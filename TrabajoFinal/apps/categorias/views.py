from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic.detail import DetailView
from .models import Comentario, Redaccion
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Formulario_Alta_Redaccion, CrearComentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.views import generic
from .filters import RedaccionFiltro
# Create your views here.
#def Listar_Noticia(request):
 #   redaccion = Redaccion.objects.all()
 #   ctx = {}
 #   ctx['p'] = redaccion
 #   return render(request,'base.html', ctx)
#class filtroviews(generic.ListView):
#	queryset = Redaccion.objects.filter(estado=True)
#	templete_name= 'categorias/listar_noticias.html'

#def FiltroViews(request):
	#context = {}

	#filtro_redaccion = RedaccionFiltro(
		#request.GET,
		#queryset = Redaccion.objects.all()
	#)

	#context['filtro_redaccion'] = filtro_redaccion

	#return render(request ,'categorias/listar_noticias.html', context=context)

class Listar_Noticia(generic.ListView):
	model = Redaccion
	template_name = 'categorias/listar_noticias.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = RedaccionFiltro(self.request.GET, queryset= self.get_queryset())
		return context


class RedactarNoticia(LoginRequiredMixin, CreateView):
	model = Redaccion
	form_class = Formulario_Alta_Redaccion
	template_name = 'nuevanoticia.html'
	success_url = reverse_lazy('categorias:noticias')



class DetalleArticulo(DetailView):
	model = Redaccion
	template_name = 'categorias/detalle_articulo.html'
	

class ComentarioViews(LoginRequiredMixin, CreateView):
	model = Comentario
	form_class = CrearComentario
	template_name = 'categorias/añadir_comentario.html'
	success_url = reverse_lazy('categorias:noticias')

	
class EditarRedaccion(LoginRequiredMixin ,UpdateView):
	model = Redaccion
	template_name = 'categorias/editar.html'
	fields = [ 'titulo', 'texto']
	success_url = reverse_lazy('categorias:noticias')