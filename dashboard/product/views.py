from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView,ListView
from django.utils.text import slugify
from product.models import Product
# Create your views here.





class CreateProduct(CreateView):
    model= Product
    fields = ['name', 'category', 'description', 'sku', 'price', 'brand','weight', ]
    template_name = 'dashbord/product/create.html'

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateProduct, self).form_valid(form)




class UpdateProduct(UpdateView):
    model= Product
    fields = ['name', 'category', 'description', 'sku', 'price', 'brand','weight', ]
    template_name = 'dashbord/product/create.html'

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateProduct, self).form_valid(form)
    

class ProductList(ListView):
    model = Product
    template_name = 'dashbord/product/list.html'
