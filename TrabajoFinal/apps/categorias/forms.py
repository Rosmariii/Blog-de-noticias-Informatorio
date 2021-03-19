from django import forms
from .models import Redaccion

class Formulario_Alta_Redaccion(forms.ModelForm):
    class Meta:
        model = Redaccion
        fields = ['titulo', 'texto', 'fecha']
