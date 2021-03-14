from django.urls import path
from . import views

app_name = 'categorias'
urlpatterns = [
    path('categoria/', views.RedactarNoticia.as_view(), name='ver'),
]