from django import forms
from django.forms import ModelForm

from .models import Proyecto


class DateInput(forms.DateInput):
    input_type = 'date'


class ProyectoForm(ModelForm):

    class Meta:
        model = Proyecto
        fields = ['codigo_proyecto', 'nombre', 'codigo_cliente', 'fecha', 'imagen']
        widgets = {
            'fecha': DateInput(),
        }