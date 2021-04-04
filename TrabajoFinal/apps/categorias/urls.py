from django.urls import path
from . import views

app_name = 'categorias'
urlpatterns = [
    path('categoria/', views.RedactarNoticia.as_view(), name='ver'),
    path('Listarnoticia/', views.Listar_Noticia.as_view(), name='noticias'),
    path('articulo/<int:pk>/', views.DetalleArticulo.as_view(), name='detallearticulo'),
    path('articulo/<int:pk>/comentario/', views.ComentarioViews.as_view(), name='nuevocoment'), 
    path('articulo/editar/<int:pk>/', views.EditarRedaccion.as_view(), name='editar'),
    path('articulo/<int:pk>/eliminar', views.EliminarRedaccion.as_view(), name='eliminar'),

]