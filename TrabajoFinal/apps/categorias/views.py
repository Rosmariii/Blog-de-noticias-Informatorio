from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Redacción
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Formulario_Alta_Redacción
from .models import Redacción
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def Listar_Noticia(request):
    redacción = Redacción.objects.all()
    ctx = {}
    ctx['p'] = redacción
    return render(request,'base.html', ctx)

class RedactarNoticia(LoginRequiredMixin, CreateView):
	model = Redacción
	form_class = Formulario_Alta_Redacción
	template_name = 'nuevanoticia.html'
	success_url = reverse_lazy('base')