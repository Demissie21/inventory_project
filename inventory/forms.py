from django import forms
from .models import Product, InventoryItem
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'description']
