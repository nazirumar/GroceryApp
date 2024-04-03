from  django.urls import path
from . import views


app_name = 'category_dashboard'

urlpatterns = [
    path('create/', views.CreateCategory.as_view(), name='category_create'),
    path('create/<int:pk>/', views.CreateSubCategory.as_view(), name='sub_category_create'),
    path('list/', views.CategoryList.as_view(), name='category_list'),
    path('<int:pk>/', views.category_detail, name='category_detail'),
    path('update/<int:pk>/', views.UpdateCategory.as_view(), name='category_update'),
]
