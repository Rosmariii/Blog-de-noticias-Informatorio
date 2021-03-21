from django import forms
from .models import Redaccion

#choices = Category.objects.all().values_list('nombre','nombre')
choices = [('Internacional', 'Internacional'), ('Policiales','Policiales'), ('Nacionales','Nacionales'), ('Deportes','Deportes')]
#choices_list = []

#for item in choices:
#    choices_list.append(item)

class Formulario_Alta_Redaccion(forms.ModelForm):
    class Meta:
        model = Redaccion
        fields = ['titulo', 'texto', 'fecha', 'categoria', 'imagen']

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'texto': forms.Textarea(attrs={'class':'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'categoria': forms.Select(choices=choices, attrs={'class':'form-control'}),
        }