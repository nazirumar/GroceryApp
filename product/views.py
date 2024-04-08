from datetime import timedelta
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView,DetailView
from product.models import Product, Category
from  checkout.forms import CheckOutLineForm
from checkout.models import Checkout, CheckoutLine

def detail_product(request, slug, form=None):
    product = get_object_or_404(Product, slug=slug)
    if not form:
        form = CheckOutLineForm(request.POST or None, product=product)
    context = {
        'object': product,
        'form': form,
    }
    return render(request, 'product/detail.html', context)


class ListProduct(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = 1

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        categories = category.get_descendants(include_self=True)
        qs = super(ListProduct, self).get_queryset().filter(
            category__in = categories
        )
        return qs

def get_or_create_checkout(request,  checkout_queryset = Checkout.objects.all()):
   user = request.user
   if request.user.is_authenticated:
       
       return checkout_queryset.get_or_create(
           user = user,
           email = request.user.email 
       )[0]
   token = request.get_signed_cookie('checkout', default=None)
   return checkout_queryset.filter(token=token,  user=None).get_or_create(
       user =None
   )[0]


def set_checkout_cookie(checkout, response):
    max_age = int(timedelta(days=30).total_seconds())
    response.set_signed_cookie('checkout', checkout.token, max_age=max_age)

def add_product_to_checkout(request, pk):
    product = get_object_or_404(Product, pk= pk)
    if request.method == 'POST':
        checkout =  get_or_create_checkout(request)
        instance = CheckoutLine(product=product, checkout=checkout)
        form = CheckOutLineForm(request.POST, instance=instance, product=product)
        if form.is_valid():
            checkout_line = CheckoutLine.objects.filter(
                product = product,
                checkout = checkout
            )
            if checkout_line.exists():
                instance = checkout_line[0]
                instance.quantity += int(request.POST.get('quantity'))
                instance.save()
            else:
                form.save()
            return HttpResponseRedirect(reverse('checkout:checkout_index'))
        else:
            response = detail_product(request, product.slug, form)
        
        if not request.user.is_authenticated:
            set_checkout_cookie(checkout, response)
        return response
    return HttpResponseRedirect(reverse('checkout:checkout_index'))
