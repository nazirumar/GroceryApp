from django.urls import path, include
from .category import urls as category_urls
from .product import urls as product_urls
from .brand import urls as brand_urls


app_name = 'dashboard'

urlpatterns = [
    path('category/', include(category_urls, namespace='category_dashboard')),
    path('product/', include(product_urls, namespace='product_dashboard')),
    path('brand/', include(brand_urls, namespace='brand_dashboard')),
]