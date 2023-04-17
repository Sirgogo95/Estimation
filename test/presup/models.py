from django.db import models



class Material(models.Model):
    codigo = models.CharField(max_length=64, primary_key=True)
    familias = models.CharField(max_length=1000, null=True, blank=True, default="")
    nombre = models.CharField(max_length=255)
    alias = models.CharField(max_length=1000, null=True, blank=True, default="")
    tasa = models.FloatField(default = 0)
    unidad = models.CharField(max_length=20)


class Suplidor(models.Model):
    suplidor = models.CharField(max_length=100, primary_key=True)
    telefono = models.CharField(max_length=100, null=True, blank=True, default="")
    ubicacion = models.CharField(max_length=255, null=True, blank=True, default="")
    correo = models.CharField(max_length=100, null=True, blank=True, default="")
    nombre_vendedor = models.CharField(max_length=100, null=True, blank=True, default="")


class Material_Analisis(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    suplidor = models.ForeignKey(Suplidor, on_delete=models.CASCADE)
    precio = models.FloatField(default = 0)
    fecha = models.DateField(null=True, blank=True, default="")
    marca = models.CharField(max_length=100, null=True, blank=True, default="")

    #precio_sin_itbis
    @property
    def precio_sin_itbis(self):
        return round(self.precio * (1 + self.material.tasa / 100),2)

    #itbis
    @property
    def itbis(self):
        return round(self.precio * (1 + self.material.tasa / 100) * 0.18,2)
    
    #precio_itbis
    @property
    def precio_itbis(self):
        return round(self.precio * (1 + self.material.tasa / 100) * 1.18,2)


class Cliente(models.Model):
    codigo_cliente = models.CharField(max_length=64, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True, default="")


class Proyecto(models.Model):
    codigo_proyecto = models.CharField(max_length=64, primary_key=True)
    codigo_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    nombre = models.CharField(max_length=200, null=True, blank=True, default="")
    fecha = models.DateField(null=True, blank=True, default="")
    