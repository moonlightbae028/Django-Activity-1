# app2/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'app2/home.html')

def products(request):
    return render(request, 'app2/products.html')

def contact(request):
    return render(request, 'app2/contact.html')
