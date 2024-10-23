# app2/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_app2'),
    path('productss/', views.products, name='products_app2'),
    path('contact/', views.contact, name='contact_app2'),
]
