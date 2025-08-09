from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

from .forms import ProductForm, InventoryItemForm
from .models import Product, InventoryItem


# ----------------------
# Authentication Views
# ----------------------

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'inventory/register.html', {'form': form})


@method_decorator(require_GET, name='dispatch')
class LogoutViewAllowGET(LogoutView):
    pass


# ----------------------
# Product Views
# ----------------------

@login_required
def home(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.all()
    return render(request, 'inventory/home.html', {'products': products})


@login_required
def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query)) if query else Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory/delete_product.html', {'product': product})


@login_required
def dashboard(request):
    products = Product.objects.all()
    total_products = products.count()
    return render(request, 'inventory/dashboard.html', {'products': products, 'total_products': total_products})


# ----------------------
# InventoryItem Views
# ----------------------

@login_required
def item_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'item_list.html', {'items': items})


@login_required
def add_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = InventoryItemForm()
    return render(request, 'add_item.html', {'form': form})


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'confirm_delete.html', {'item': item})
