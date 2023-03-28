from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Material

# Create your views here.
def index(request):
    return render(request, "presup/index.html")


def analisis(request):
    return render(request, "presup/analisis.html")


def precios(request):
    return render(request, "presup/precios.html")



def material(request): 
    if request.method == 'POST':
        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        tasa = float(request.POST["tasa"])
        unidad = request.POST["unidad"]
        alias = request.POST["alias"]
        familias = request.POST["familias"]

        x = Material(codigo = codigo, nombre = nombre,tasa = tasa, unidad = unidad, alias = alias, familias = familias)
        x.save()       
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
    listado = Material.objects.all()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

