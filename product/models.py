from django.db import models
from django.urls import reverse_lazy
from mptt.models import MPTTModel
from mptt.managers import TreeManager

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    background_image = models.ImageField(null=True, blank=True, upload_to='category_background')
    

    tree = TreeManager()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("dashboard:category_dashboard:category_list")

   
    
    

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse_lazy("dashboard:brand_dashboard:brand_list")
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    weight = models.FloatField()
    sku = models.CharField(max_length=30, unique=True)
    stock = models.PositiveIntegerField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("dashboard:product_dashboard:product_list")
    
    def get_thumbnail(self):
        return self.productimage_set.first()

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    alt = models.CharField(max_length=255)

    def __str__(self):
        return self.alt
    




