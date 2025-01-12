from django.db import models

# Create your models here.

class tablaPrueva(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)
    
    imajen = models.ImageField(upload_to="imagenes/", null=True)
    def __str__(self):
        return self.nombre
    
class tablaVinculada(models.Model):
    nombre = models.CharField(max_length=50)
    tablaPrueva = models.ForeignKey(tablaPrueva, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

