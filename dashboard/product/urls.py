from django.urls import path
from . import views
from dashboard.decorators import user_dashboard_permissions

app_name = 'product_dashboard'

urlpatterns = [
    path('create/', user_dashboard_permissions(views.CreateProduct.as_view()), name='product_create'),
    path('list/', user_dashboard_permissions(views.ProductList.as_view()), name='product_list'),
    path('update/<int:pk>/', user_dashboard_permissions(views.UpdateProduct.as_view()), name='product_update'),
    path('<int:pk>/list/images/', user_dashboard_permissions(views.ProductImageList.as_view()), name='product_image_list'),
    path('<int:pk>/create/image/', user_dashboard_permissions(views.create_image), name='create_image'),
    path('delete/image/<int:pk>/', user_dashboard_permissions(views.delete_image), name='delete_image'),
    path('delete/<int:pk>/', user_dashboard_permissions(views.delete_product), name='delete_product'),
    
]

