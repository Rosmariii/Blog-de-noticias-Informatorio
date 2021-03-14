from django.urls import path
from . import views
from .views import RegistroUsuario

app_name = 'usuario'
urlpatterns = [
#    path("Newnoticia/", views.noticia , name= "nueva_noticia"),
    path("registro/", RegistroUsuario.as_view(), name= "registrar"),
]