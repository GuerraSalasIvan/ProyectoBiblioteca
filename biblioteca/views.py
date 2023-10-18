from django.shortcuts import render
from .models import *

# Create your views here.
def indice(request):
    return render(request, 'index.html', {})

def listar_libros(request):
    #libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    
    libros = Libro.objects.all
    
    return render(request, 'libro_listar.html', {'libros_mostrar':libros})