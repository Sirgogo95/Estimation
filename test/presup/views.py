from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Material, Suplidor, Material_Analisis, Cliente, Proyecto
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProyectoForm, MaterialForm, SuplidorForm, PreciosForm
from django_htmx.http import trigger_client_event

# Create your views here.
def index(request):
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all().order_by('suplidor').values()
    return render(request, "presup/index.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor})


def analisis(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ProyectoForm()
    return render(request, "presup/analisis.html", {"form":form})

def analisis2(request, pk):
    if request.method == "POST":
        x= Proyecto.objects.get(codigo_proyecto = pk)
        x.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def precios(request):
    listado_precios = Material_Analisis.objects.all()
    return render(request, "presup/precios.html", {"listado_precios":listado_precios})


def add_precios(request):
    name = "Agregar Precios"
    data_path = "precios" 
    if request.method == "POST":
        form = PreciosForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse(status=200)
            return trigger_client_event(response,"edit_precios",{})
    else:
        form = PreciosForm()
        return render(request, "presup/base_modal.html", {"form":form, "name":name, "data_path":data_path})


def edit_precios(request, pk):
    name = "Editar Precios"
    data_path = "precios"
    x= Material_Analisis.objects.get(id = pk)
    if request.method == "POST":
        form = PreciosForm(request.POST, instance=x)
        if form.is_valid():          
            form.save()
            response = HttpResponse(status=200)
            return trigger_client_event(response,"edit_precios",{})
    else:
        form = PreciosForm(instance = x)
        return render(request, "presup/base_modal.html", {"form":form, "name":name, "data_path":data_path})
        

def delete_precios(request, pk):
    name = "Eliminar Precios"
    data_path = "precios"
    if request.method == 'POST':
        x = Material_Analisis.objects.get(id=pk)
        x.delete()
        response = HttpResponse(status=200)
        return trigger_client_event(response,"edit_precios",{})
    else:
        return render(request, "presup/delete_modal.html", {"name":name, "data_path":data_path})











def material(request):
    listado = Material.objects.all()
    return render(request, "presup/material.html", {"listado":listado})


def add_material(request):
    name = "Agregar Material"
    data_path = "material" 
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse(status=200)
            return trigger_client_event(response,"edit_material",{})
    else:
        form = MaterialForm()
        return render(request, "presup/base_modal.html", {"form":form, "name":name, "data_path":data_path})


def edit_material(request, pk):
    name = "Editar Material"
    data_path = "material"
    x= Material.objects.get(codigo = pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=x)
        if form.is_valid():          
            form.save()
            response = HttpResponse(status=200)
            return trigger_client_event(response,"edit_material",{})
    else:
        form = MaterialForm(instance = x)
        return render(request, "presup/base_modal.html", {"form":form, "name":name, "data_path":data_path})
        

def delete_material(request, pk):
    name = "Eliminar Material"
    data_path = "material"
    if request.method == 'POST':
        x = Material.objects.get(codigo=pk)
        x.delete()
        response = HttpResponse(status=200)
        return trigger_client_event(response,"edit_material",{})
    else:
        return render(request, "presup/delete_modal.html", {"name":name, "data_path":data_path})










def suplidor(request):      
    listado = Suplidor.objects.all()
    return render(request, "presup/suplidor.html", {"listado":listado})

def add_suplidor(request):
    name = "Agregar Suplidor"
    data_path = "suplidor"
    if request.method == "POST":
        form = SuplidorForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse(status=200)
            return trigger_client_event(response,"edit_suplidor",{})
    else:
        form = SuplidorForm()
        return render(request, "presup/base_modal.html", {"form":form, "name":name, "data_path":data_path})

def edit_suplidor(request, pk):
    name = "Editar Suplidor"
    data_path = "suplidor"
    x= Suplidor.objects.get(suplidor = pk)
    if request.method == "POST":
        form = SuplidorForm(request.POST, instance=x)
        if form.is_valid():          
            form.save()
            response = HttpResponse(status=200)
            return trigger_client_event(response,"edit_suplidor",{})
    else:
        form = SuplidorForm(instance = x)
        return render(request, "presup/base_modal.html", {"form":form, "name":name, "data_path":data_path})
 

def eliminar_suplidor(request, pk):
    name = "Eliminar Suplidor"
    data_path = "suplidor"
    if request.method == 'POST':
        x = Suplidor.objects.get(suplidor=pk)
        x.delete()
        response = HttpResponse(status=200)
        return trigger_client_event(response,"edit_suplidor",{})
    else:
        return render(request, "presup/delete_modal.html", {"name":name, "data_path":data_path})







































def cliente(request):  
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all().order_by('suplidor').values()        
    listado = Cliente.objects.all()
    return render(request, "presup/cliente.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor, "listado":listado})

def add_cliente(request): 
    if request.method == 'POST':
        codigo = request.POST["cliente_codigo"]
        nombre = request.POST["cliente_nombre"]
       
        x = Cliente(codigo_cliente = codigo, nombre = nombre) 
        x.save() 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def proyecto(request):  
    listado_material = Material.objects.all().order_by('nombre').values()
    listado_suplidor = Suplidor.objects.all().order_by('suplidor').values()        
    listado = Suplidor.objects.all()
    return render(request, "presup/proyecto.html", {"listado_material":listado_material, "listado_suplidor":listado_suplidor, "listado":listado})