from django.urls import path
from checkout import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout_view, name='checkout_index'),
    path('create/address/', views.create_shipping_adresses, name='checkout_create_address'),
    path('edit/address/', views.edit_shipping_adresses, name='checkout_edit_address'),
    path('create/order/', views.create_order_view, name='create_order_view'),
]
