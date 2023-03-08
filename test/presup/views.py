from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "presup/index.html")


def analisis(request):
    return render(request, "presup/analisis.html")