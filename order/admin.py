from django.contrib import admin
from  order.models import Order, OrderLine
# Register your models here.

admin.site.register(OrderLine)

admin.site.register(Order)