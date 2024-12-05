"""Este módulo contiene las definiciones de los modelos de la tienda de cafe"""
from django.contrib.auth.models import AbstractUser
#from django.core.exceptions import ValidationError
from django.db import models


class Producto(models.Model):
    """Clase que representa un producto en la tienda."""

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return str (self.nombre)

class Usuario(AbstractUser):

    nomApe= models.CharField("Nombre y Apellido",max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nomApe)

class Carrito(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="carrito")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Carrito de {self.user.nomApe}"

    @property
    def total(self):
        return self.producto.precio * self.cantidad














# Create your models here.
