from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView,ListView
from django.utils.text import slugify
from product.models import Brand
# Create your views here.





class CreateBrand(CreateView):
    model= Brand
    fields = ['name', 'image']
    template_name = 'dashboard/brand/create.html'

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateBrand, self).form_valid(form)




class UpdateBrand(UpdateView):
    model= Brand
    fields = ['name', 'image']
    template_name = 'dashboard/brand/create.html'

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateBrand, self).form_valid(form)
    

class BrandList(ListView):
    model = Brand
    template_name = 'dashboard/brand/list.html'



def delete_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if brand:
        brand.delete()
        return JsonResponse({'message': 'Brand  deleted successfully'}, status=200)
    return JsonResponse({'message':'this Brand  instance does not exist'}, status=400)
