"""Este módulo contiene las definiciones de los modelos de la tienda de cafe"""

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




# Create your models here.
