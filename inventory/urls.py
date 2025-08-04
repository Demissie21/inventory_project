from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.LogoutViewAllowGET.as_view(), name='logout'),
]
