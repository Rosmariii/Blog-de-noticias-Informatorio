from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    nombre = CharField(max_length=50)

    def __str__(self):
        return (self.nombre)

    def get_absolute_url(self):
        return reverse('base')
#categorias_status=[
#    (1, 'Internacionales'),
#    (2, 'Nacionales'),
#    (3, 'Policiales'),
#    (4, 'Deportes'),
#]

class Redaccion(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField() 
    fecha = models.DateField(default=timezone.now)
    categoria = models.CharField(max_length=255, default='coding')
    imagen = models.ImageField(null=True, blank=True, upload_to='image/')

    def __str__(self):
        return (self.titulo)

    def get_absolute_url(self):
        return reverse('base')