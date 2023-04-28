from django import forms
from django.forms import ModelForm

from .models import Material, Suplidor, Material_Analisis, Proyecto


class DateInput(forms.DateInput):
    input_type = 'date'

class ProyectoForm(ModelForm):

    class Meta:
        model = Proyecto
        fields = ['codigo_proyecto', 'nombre', 'codigo_cliente', 'fecha', 'imagen']
        widgets = {
            'fecha': DateInput(),
        }

class MaterialForm(ModelForm):

    class Meta:
        model = Material
        fields = ['codigo', 'familias', 'nombre', 'alias', 'tasa', 'unidad']
       

class SuplidorForm(ModelForm):

    class Meta:
        model = Suplidor
        fields = ['suplidor', 'telefono', 'ubicacion', 'correo', 'nombre_vendedor']


class PreciosForm(ModelForm):

    class Meta:
        model = Material_Analisis
        fields = ['material', 'suplidor', 'precio', 'fecha', 'marca']
        widgets = {
            'fecha': DateInput(),
        }