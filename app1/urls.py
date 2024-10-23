# app1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base_app1'),
    path('home/', views.home, name='home_app1'),
    path('about/', views.about, name='about_app1'),
    path('contact/', views.contact, name='contact_app1'),
]
