
from django.urls import path
from .import views
from dashboard.decorators import user_dashboard_permissions


app_name = 'brand_dashboard'


urlpatterns = [
    path('create/', user_dashboard_permissions(views.CreateBrand.as_view()), name='brand_create'),
    path('list/', user_dashboard_permissions(views.BrandList.as_view()), name='brand_list'),
    path('update/<int:pk>/', user_dashboard_permissions(views.BrandList.as_view()), name='brand_update'),
    path('delete/<int:pk>/', user_dashboard_permissions(views.delete_brand), name='delete_brand'),

   
    
]
