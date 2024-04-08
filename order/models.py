from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

ORDER_STATUS =(
    (0, 'Unfullfiled'),
    (1, 'Fullfiled'),
    (2, 'Canceled'),
    (3, 'Refunded'),
)
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=ORDER_STATUS, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    checkout_token = models.CharField(max_length=226,default="")
    note = models.TextField(blank=True, default="")
    shipping =models.ForeignKey('userprofile.Adresses', on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    

    def __str__(self):
        return self.email



class OrderLine(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE,  editable=False)
    product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, blank=True, null=True)
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    sku = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return "{}x{}".format(self.product_name, self.product_price)
    
    
    def get_subtotal(self):
        return self.product.price * self.quantity

