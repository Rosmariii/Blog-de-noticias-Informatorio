from django import forms
from .models import Redacción

class Formulario_Alta_Redacción(forms.ModelForm):
    class Meta:
        model = Redacción
        fields = ['titulo', 'texto', 'categoria', 'imagen']
