"""
mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indice, name='indice'),
    
    path('libros/listar', views.listar_libros, name='lista_libros'),
    
    path('libros/<int:id_libro>/', views.dame_libro, name='dame_libro'),
    
    
    path('cliente/listar', views.listar_cliente, name='lista_cliente'),
    
    path('cliente/<int:id_cliente>/', views.dame_cliente, name='dame_cliente'),
    
    
    path('biblioteca/listar', views.listar_biblioteca, name='lista_biblioteca'),
    
    path('biblioteca/<int:id_biblioteca>/', views.dame_biblioteca, name='dame_biblioteca'),
    
    
]
