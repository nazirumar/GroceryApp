from django.contrib import admin
from checkout.models import Checkout,CheckoutLine


admin.site.register(CheckoutLine)

admin.site.register(Checkout)
