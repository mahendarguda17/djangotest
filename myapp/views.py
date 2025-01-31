from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'home.html', {'products': products})
