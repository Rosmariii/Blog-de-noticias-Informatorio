from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Redaccion
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Formulario_Alta_Redaccion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.
#def Listar_Noticia(request):
 #   redaccion = Redaccion.objects.all()
 #   ctx = {}
 #   ctx['p'] = redaccion
 #   return render(request,'base.html', ctx)

class Listar_Noticia(ListView):
    model = Redaccion
    template_name = 'categorias/listar_noticias.html'

class RedactarNoticia(LoginRequiredMixin, CreateView):
	model = Redaccion
	form_class = Formulario_Alta_Redaccion
	template_name = 'nuevanoticia.html'
	success_url = reverse_lazy('base')