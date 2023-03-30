from django.db import models



class Material(models.Model):
    codigo = models.CharField(max_length=64, primary_key=True)
    familias = models.CharField(max_length=1000, null=True, blank=True, default="")
    nombre = models.CharField(max_length=255)
    alias = models.CharField(max_length=1000, null=True, blank=True, default="")
    tasa = models.FloatField(default = 0.0)
    unidad = models.CharField(max_length=20)


class Suplidor(models.Model):
    suplidor = models.CharField(max_length=100, primary_key=True)
    telefono = models.CharField(max_length=100, null=True, blank=True, default="")
    ubicacion = models.CharField(max_length=255, null=True, blank=True, default="")
    correo = models.CharField(max_length=100, null=True, blank=True, default="")
    nombre_vendedor = models.CharField(max_length=100, null=True, blank=True, default="")


