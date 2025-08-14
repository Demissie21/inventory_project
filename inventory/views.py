from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Product


from django.shortcuts import render, redirect
from .forms import ProductForm
from django.shortcuts import render, redirect
from .forms import ProductForm  # Make sure ProductForm exists

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # or wherever you list products
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to product list view
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def inventory_dashboard(request):
    products = Product.objects.all()
    return render(request, 'inventory/dashboard.html', {'products': products})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(request, 'inventory/delete_confirm.html', {'product': product})
