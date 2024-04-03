from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView,ListView
from django.utils.text import slugify
from product.models import Brand
# Create your views here.





class CreateBrand(CreateView):
    model= Brand
    fields = ['name', 'image']
    template_name = 'dashbord/brand/create.html'

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateBrand, self).form_valid(form)




class UpdateBrand(UpdateView):
    model= Brand
    fields = ['name', 'image']
    template_name = 'dashbord/brand/create.html'

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateBrand, self).form_valid(form)
    

class BrandList(ListView):
    model = Brand
    template_name = 'dashbord/brand/list.html'
