from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from checkout.decorator import user_cookie_checkout
from checkout.models import CheckoutLine, Checkout
from order.models import Order, OrderLine
from userprofile.form import ShippingAddressForm, VisitorShippingAddressForm, EditShippingAddressForm
from userprofile.models import UserProfile, Adresses
# Create your views here.


def get_checkout(request):
   user = request.user
   if user.is_authenticated:
       return Checkout.objects.get(user=user, email=user.email)
   token = request.get_signed_cookie('checkout')
   print(token)
   return Checkout.objects.get(user=None, token=token)


def checkout_view(request):
    is_none= False
    try:
        checkout = get_checkout(request)
    except Checkout.DoesNotExist:
        is_none = True

    if (not request.user.is_authenticated and request.get_signed_cookie('checkout', None) is None) or is_none:
        context ={
            'checkout_line': None
        }
        return TemplateResponse(request,'checkout/index.html', context)
    context = {
        'checkout_line': CheckoutLine.objects.filter(checkout=checkout),
        'checkout':checkout
    }
    return TemplateResponse(request, 'checkout/index.html', context)

@user_cookie_checkout
def create_shipping_adresses(request):
    checkout = get_checkout(request)
    print(checkout)
    user = request.user
    is_auth = user.is_authenticated
    if is_auth:
        form = ShippingAddressForm(request.POST or None)
    else:
        form = VisitorShippingAddressForm(request.POST or None, instance=checkout.shipping)

    context = {
        'form': form
    }
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            if is_auth:
                profile = get_object_or_404(UserProfile, user=user)
                profile.user_adress.add(obj)
                profile.save()
            else:
                checkout.email = request.POST.get('email')
            checkout.shipping = obj
            checkout.save()
            return HttpResponseRedirect(reverse('checkout:create_order_view'))

    else:
        if is_auth:
            address_form = EditShippingAddressForm(user=user)
            context.update({'address_form': address_form})
    return TemplateResponse(request, 'checkout/shipping_create.html', context)

                
@user_cookie_checkout
def edit_shipping_adresses(request):
    user = request.user
    if user.is_authenticated and request.method == 'POST':
        form = EditShippingAddressForm(request.POST, user=user)
        if form.is_valid():
            checkout = get_checkout(request)
            checkout.shipping = Adresses.objects.get(id=int(request.POST.get('address')))
            checkout.save()
            return HttpResponseRedirect(reverse('checkout:create_order_view'))
    return HttpResponseRedirect(reverse('checkout:create_order_view'))
    
        


@user_cookie_checkout
def create_order_view(request):
    checkout = get_checkout(request)
    checkout_line = checkout.checkoutline_set.all()
    user = request.user
    if request.method == 'POST':
        if checkout_line.count() > 0:
            if user.is_authenticated:
                order = Order.objects.create(
                    checkout_token=checkout.token,
                      user=user,
                      email = user.email,
                      shipping = checkout.shipping
                )
            else:
                order = Order.objects.create(
                    checkout_token=checkout.token,
                      email = checkout.email,
                      shipping = checkout.shipping
                )
            
            total = 0
            for line in checkout_line:
                product = line.product
                order_line = OrderLine.objects.create(
                    order=order,
                    product=product,
                    product_name=product.name,
                    product_price=product.price,
                    quantity=line.quantity,
                    sku=product.sku)
                total += order_line.get_subtotal()
            order.total = total
            order.save()
            checkout.delete()
            response = HttpResponseRedirect(reverse('order:detail_order', kwargs={
                'pk': order.id,
    
            }))
            response.delete_cookie('checkout', None)
            return response
    context={
            'checkout_line': checkout_line,
            'checkout':checkout
                }
    return TemplateResponse(request, 'checkout/confirm_order.html', context)


