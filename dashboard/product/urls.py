from django.urls import path
from . import views
app_name = 'product_dashbord'

urlpatterns = [
    path('create/', views.CreateProduct.as_view(), name='create_product'),
    path('list/', views.ProductList.as_view(), name='product_list'),
    path('update/<int:pk>/', views.UpdateProduct.as_view(), name='product_update'),
    
]

