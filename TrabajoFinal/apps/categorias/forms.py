from django import forms
from .models import Comentario, Redaccion


choices = [('Internacional', 'Internacional'), ('Policiales','Policiales'), ('Nacionales','Nacionales'), ('Deportes','Deportes')]

class Formulario_Alta_Redaccion(forms.ModelForm):
    class Meta:
        model = Redaccion
        fields = ['titulo', 'texto', 'fecha', 'autor', 'categoria']

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'texto': forms.Textarea(attrs={'class':'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'categoria': forms.Select(choices=choices, attrs={'class':'form-control'}),
        }
    
class CrearComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['post','nombre', 'cuerpo']

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),

        }