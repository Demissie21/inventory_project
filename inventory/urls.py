from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Inventory item URLs
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
]
