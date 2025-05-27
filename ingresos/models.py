from django.db import models



class Ingreso(models.Model):
    idIngreso = models.CharField(max_length=100)
    idProducto = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)

    def __str__(self):
        return self.idIngreso 


# Create your models here.
