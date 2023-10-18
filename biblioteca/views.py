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