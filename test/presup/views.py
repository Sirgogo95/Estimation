from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Material, Suplidor, Material_Analisis

# Create your views here.
def index(request):
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all().order_by('suplidor').values()
    return render(request, "presup/index.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor})


def analisis(request):
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all().order_by('suplidor').values()
    return render(request, "presup/analisis.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor})


def precios(request):
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all().order_by('suplidor').values()
    listado_precios = Material_Analisis.objects.all()
    return render(request, "presup/precios.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor, "listado_precios":listado_precios})


def add_precios(request):
    if request.method == 'POST':
        codigo = request.POST["precios_codigo"]
        suplidor = request.POST["precios_suplidor"]
        precio = request.POST["precios_precio"]
        marca = request.POST["precios_marca"]
        fecha = request.POST["precios_fecha"]


        mat = Material.objects.get(codigo=codigo)
        sup = Suplidor.objects.get(suplidor=suplidor)
        x= Material_Analisis(material = mat, suplidor = sup, precio = precio, marca = marca, fecha = fecha)
        x.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def eliminar_precios(request):
    if request.method == 'POST':
        codigo = request.POST["precios_codigo_eliminar"]
        suplidor = request.POST["precios_suplidor_eliminar"]
        precio = request.POST["precios_precio_eliminar"]
        marca = request.POST["precios_marca_eliminar"]
        fecha = request.POST["precios_fecha_eliminar"]

    
        mat = Material.objects.get(codigo=codigo)
        sup = Suplidor.objects.get(suplidor=suplidor)
        x= Material_Analisis.objects.get(material = mat, suplidor = sup, precio = precio, marca = marca, fecha = fecha)
        x.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def material(request):
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all() .order_by('suplidor').values()     
    listado = Material.objects.all()
    return render(request, "presup/material.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor, "listado":listado})


def add_material(request):
    if request.method == 'POST':
        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        tasa = float(request.POST["tasa"])
        unidad = request.POST["unidad"]
        alias = request.POST["alias"]
        familias = request.POST["familias"]

        x = Material(codigo = codigo, nombre = nombre,tasa = tasa, unidad = unidad, alias = alias, familias = familias)
        x.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eliminar_material(request):
    if request.method == 'POST':
        codigo = request.POST["codigo-eliminar"]

        x = Material.objects.get(codigo=codigo)
        x.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def suplidor(request):  
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all().order_by('suplidor').values()        
    listado = Suplidor.objects.all()
    return render(request, "presup/suplidor.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor, "listado":listado})

def add_suplidor(request):
    if request.method == 'POST':
        suplidor = request.POST["suplidor"]
        telefono = request.POST["telefono"]
        ubicacion = request.POST["ubicacion"]
        correo = request.POST["correo"]
        nombre_vendedor = request.POST["nombre_vendedor"]

        x = Suplidor(suplidor = suplidor, telefono = telefono, ubicacion = ubicacion, correo = correo, nombre_vendedor = nombre_vendedor)
        x.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eliminar_suplidor(request):
    if request.method == 'POST':
        suplidor = request.POST["suplidor-eliminar"]

        x = Suplidor.objects.get(suplidor=suplidor)
        x.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def proyecto(request):  
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all().order_by('suplidor').values()        
    listado = Suplidor.objects.all()
    return render(request, "presup/proyecto.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor, "listado":listado})