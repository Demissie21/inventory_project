from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_dashboard, name='dashboard'),
    path('add/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('register/', views.register_user, name='register'),
]
