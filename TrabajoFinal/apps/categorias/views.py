from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .models import Comentario, Redaccion
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import Formulario_Alta_Redaccion, CrearComentario
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

class DetalleArticulo(DetailView):
	model = Redaccion
	template_name = 'categorias/detalle_articulo.html'
	success_url = reverse_lazy('base')

class ComentarioViews(CreateView):
	model = Comentario
	form_class = CrearComentario
	template_name = 'categorias/añadir_comentario.html'
	success_url = reverse_lazy('base')
	
	