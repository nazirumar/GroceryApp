
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView,ListView
from django.utils.text import slugify
from dashboard.product.forms import ProductImageForm
from product.models import Product, ProductImage
from django.http import JsonResponse
# Create your views here.





class CreateProduct(CreateView):
    model= Product
    fields = ['name', 'description', 'sku', 'price', 'brand', 'stock', 'category', 'weight' ]
    template_name = 'dashboard/product/create.html'

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateProduct, self).form_valid(form)




class UpdateProduct(UpdateView):
    model= Product
    fields = ['name', 'category', 'description', 'sku', 'price', 'brand','weight', ]
    template_name = 'dashboard/product/create.html'

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateProduct, self).form_valid(form)
    

class ProductList(ListView):
    model = Product
    template_name = 'dashboard/product/list.html'

class ProductImageList(ListView):
    model = ProductImage
    template_name = 'dashboard/product/list_image.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductImageList, self).get_context_data(**kwargs)
        context["form"] = ProductImageForm()
        context["product_id"] = self.kwargs.get('pk') 
        return context
    
    def get_queryset(self):
        return super(ProductImageList, self).get_queryset().filter(product__id = self.kwargs.get('pk'))
    

def create_image(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductImageForm(request.POST, request.FILES)
    print(form)
    
    if form.is_valid():
        image_obj = form.save(commit=False)
        image_obj.product = product
        image_obj.alt = product.name
        image_obj.save()
        return JsonResponse({
                'message': 'Product image created successfully', 
                'url': image_obj.image.url,
                'alt': image_obj.alt,
                'delete_url': reverse('dashboard:product_dashboard:delete_image', kwargs={
                'pk': image_obj.id,
                    })},
                status=200)
    return JsonResponse({'error':'Failed to create product image', 'errors': form.errors}, status=400)
  

def delete_image(request, pk):
    product_image = get_object_or_404(ProductImage, pk=pk)
    if product_image:
        product_image.delete()
        return JsonResponse({'message': 'Product image deleted successfully'}, status=200)
    return JsonResponse({'message':'this product image instance does not exist'}, status=400)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product:
        product.delete()
        return JsonResponse({'message': 'Product  deleted successfully'}, status=200)
    return JsonResponse({'message':'this product  instance does not exist'}, status=400)
