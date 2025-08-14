from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_dashboard, name='dashboard'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
