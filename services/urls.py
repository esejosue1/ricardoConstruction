
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('<slug:slug_detail>/', views.serviceDetail, name='serviceDetail')
]
