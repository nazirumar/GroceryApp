from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView,ListView
from django.utils.text import slugify
from product.models import Category, Brand
# Create your views here.


class CreateCategory(CreateView):
    model = Category
    fields = ['name', 'description', 'background_image']
    template_name = 'dashbord/category/create.html'
    # success_url = reverse('
    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateCategory, self).form_valid(form)
    


class UpdateCategory(UpdateView):
    model = Category
    fields = ['name', 'description', 'background_image']
    template_name = 'dashbord/category/create.html'

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateCategory, self).form_valid(form)

class CreateSubCategory(CreateView):
    model = Category
    fields = ['name', 'description', 'background_image']
    template_name = 'dashbord/category/create.html'

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.parent = Category.objects.get(id=int(self.kwargs.get('pk')))
        instance.save()
        return super(CreateSubCategory, self).form_valid(form)


class CategoryList(ListView):
    model = Category
    template_name = 'dashbord/category/list.html'



def category_detail(request, pk):
    root = get_object_or_404(Category, pk=pk)
    path = root.get_ancestors(include_self=True)
    categories = root.get_children().order_by('name')
    context ={
        'categories': categories,
        'path': path,
        'root': root,
        
        }
    return render(request, 'dashbord/category/detail.html', context)

