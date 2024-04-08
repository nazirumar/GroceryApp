from  django.urls import path
from product import views

app_name = 'products'

urlpatterns = [
    path('<str:slug>/', views.detail_product, name='detail_product'),
    path('category/<str:slug>/', views.ListProduct.as_view(), name='list_product'),
    path('add/<int:pk>/', views.add_product_to_checkout, name='add_product_to_checkout')
]
