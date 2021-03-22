from django.urls import path
from . import views

app_name = 'categorias'
urlpatterns = [
    path('categoria/', views.RedactarNoticia.as_view(), name='ver'),
    path('Listarnoticia/', views.Listar_Noticia.as_view(), name='noticias'),
    path('articulo/', views.DetalleArticulo.as_view(), name='detallearticulo'),
    path('comentario/', views.ComentarioViews.as_view(), name='nuevocoment'),    
]