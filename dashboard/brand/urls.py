
from django.urls import path
from .import views
app_name = 'brand_dashbord'


urlpatterns = [
    path('create/', views.CreateBrand.as_view(), name='create_brand'),
    path('list/', views.BrandList.as_view(), name='brand_list'),
    path('update/<int:pk>/', views.BrandList.as_view(), name='brand_update'),
   
    
]
