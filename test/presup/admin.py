from django.contrib import admin
from .models import Material, Suplidor, Material_Analisis, Proyecto, Cliente


# Register your models here.
admin.site.register(Material)
admin.site.register(Suplidor)
admin.site.register(Material_Analisis)
admin.site.register(Cliente)
admin.site.register(Proyecto)