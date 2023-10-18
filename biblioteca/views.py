from django.shortcuts import render
from .models import *

# Create your views here.
def indice(request):
    return render(request, 'index.html', {})

def listar_libros(request):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    
    return render(request, 'libro/libro_listar.html', {'libros_mostrar':libros})

def dame_libro(request, id_libro):
    libro = Libro.objects.select_related('biblioteca').prefetch_related('autores').get(id=id_libro)
    
    return render (request, 'libro/dame_libro.html', {'libro':libro})



def listar_cliente(request):
    cliente = Cliente.objects.all
    
    return render(request, 'cliente/cliente_listar.html', {'cliente_mostrar':cliente})

def dame_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    
    return render (request, 'cliente/dame_cliente.html', {'cliente':cliente})



def listar_biblioteca(request):
    biblioteca = Biblioteca.objects.all
    
    return render(request, 'biblioteca/biblioteca_listar.html', {'biblioteca_mostrar':biblioteca})

def dame_biblioteca(request, id_biblioteca):
    biblioteca = Libro.objects.get(id=id_biblioteca)
    
    return render (request, 'biblioteca/dame_biblioteca.html', {'biblioteca':biblioteca})