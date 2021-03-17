from django.db import models


# Create your models here.
#categorias_status=[
#    (1, 'Internacionales'),
#    (2, 'Nacionales'),
#    (3, 'Policiales'),
#    (4, 'Deportes'),
#]

class Redacción(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField() 
    fecha = models.DateTimeField(auto_now_add=True)
  #  categoria = models.IntegerField(
  #      null=False, blank=False,
  #      choices=categorias_status
  #  )
#    imagen = models.ImageField()

    def __str__(self):
        return (self.nombre)