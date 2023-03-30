from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Material, Suplidor

# Create your views here.
def index(request):
    return render(request, "presup/index.html")


def analisis(request):
    return render(request, "presup/analisis.html")


def precios(request):
    return render(request, "presup/precios.html")



def material(request):      
    listado = Material.objects.all()
    return render(request, "presup/material.html", {"listado":listado})


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
    listado = Suplidor.objects.all()
    return render(request, "presup/suplidor.html", {"listado":listado})

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
