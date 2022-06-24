from dataclasses import field
from pyexpat import model
from django import forms
from .models import TablaEmpleado, TablaNomina

class NominaForm(forms.ModelForm):

    class Meta:
        model = TablaNomina
        fields = ('__all__')

class EmpleadosForm(forms.ModelForm):

    class Meta:
        model = TablaEmpleado
        fields = ('__all__')