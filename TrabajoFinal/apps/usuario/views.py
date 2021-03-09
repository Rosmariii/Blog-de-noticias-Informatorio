from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

def noticia(request):
	return render(request,"admi/nuevanoticia.html")

class RegistroUsuario(CreateView):
	model = User
	template_name = 'admi/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('base')