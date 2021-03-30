from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    nombre = CharField(max_length=50)

    def __str__(self):
        return (self.nombre)

    def get_absolute_url(self):
        return reverse('base')

class Redaccion(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField() 
    fecha = models.DateField(default=timezone.now)
    categoria = models.CharField(max_length=255, default='coding')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    #imagen = models.ImageField(null=True, blank=True, upload_to='categorias/')

    def __str__(self):
        return self.titulo 


class Comentario(models.Model):
    post = models.ForeignKey(Redaccion, related_name='comentarios', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha_comentario = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
