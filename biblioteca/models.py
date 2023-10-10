from django.db import models
from django.utils import timezone


# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField
    fechaCreacion = models.DateTimeField(default=timezone.now)
    telefono = models.IntegerField
    
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200, blank=True)
    edad = models.IntegerField(null = True)
    
    
class Libro(models.Model):
    IDIOMAS = [
        ('ES','Español'),
        ('EN','Inglés'),
        ('FR','Frances'),
        ('IT','Italiano'),
    ]
    
    nombre = models.CharField(max_length=200)
    idioma = models.CharField(
        max_length = 2,
        choices= IDIOMAS,
        default = 'ES'
    )
    
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    ISBN = models.CharField(max_length=200, unique=True)
    
    
    GENEROS = [
        ('TR','Terror'),
        ('MS','Misterio'),
        ('FN','Fantasia'),
        ('CF','Ciencia Ficción'),
        ('SP','Suspense'),
    ]    
    
    genero = models.CharField(
        max_length = 2,
        choices= GENEROS,
    )
    
    biblioteca = models.ForeignKey(Biblioteca, on_delete = models.CASCADE)
    
    autores =   models.ManyToManyField(Autor)
     
     
class Cliente(models.Model):
    nombre =models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email =models.CharField(max_length=200, unique=True)
    puntos = models.FloatField(default=5.0, db_column="puntos_biblioteca")
    telefono = models.IntegerField()
    dni = models.CharField(unique=True, max_length=30)
    
    
class DatosCliente(models.Model):
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField()
    altura = models.FloatField()
    peso = models.FloatField()
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    
class Prestamo(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now)