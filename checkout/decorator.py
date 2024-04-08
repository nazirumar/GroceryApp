from checkout.models import Checkout
from django.http import HttpResponseRedirect
from django.urls  import reverse

def user_cookie_checkout(viewfunc):
    def wrapper_function(request, *args, **kwargs):
        response = HttpResponseRedirect(reverse('checkout:checkout_index'))
        if not  request.user.is_authenticated:
            checkout_token = request.get_signed_cookie('checkout', None)
            if checkout_token is None:
                return response
            else:
                checkout = Checkout.objects.filter(token=checkout_token)
                if not checkout.exists():
                    return response
        else:
            checkout = Checkout.objects.filter(user=request.user, email=request.user.email)
            if not checkout.exists():
                return response
        return viewfunc(request, *args, **kwargs)
    return wrapper_function


