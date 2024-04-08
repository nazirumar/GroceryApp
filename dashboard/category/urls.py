from  django.urls import path
from . import views
from dashboard.decorators import user_dashboard_permissions

app_name = 'category_dashboard'

urlpatterns = [
    path('create/', user_dashboard_permissions(views.CreateCategory.as_view()), name='category_create'),
    path('create/<int:pk>/', user_dashboard_permissions(views.CreateSubCategory.as_view()), name='sub_category_create'),
    path('list/', user_dashboard_permissions(views.CategoryList.as_view()), name='category_list'),
    path('<int:pk>/', user_dashboard_permissions(views.category_detail), name='category_detail'),
    path('update/<int:pk>/', user_dashboard_permissions(views.UpdateCategory.as_view()), name='category_update'),
    path('delete/<int:pk>/', user_dashboard_permissions(views.delete_category), name='delete_category'),

]
