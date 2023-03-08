from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "presup/index.html")


def analisis(request):
    return render(request, "presup/analisis.html")


def precios(request):
    return render(request, "presup/precios.html")