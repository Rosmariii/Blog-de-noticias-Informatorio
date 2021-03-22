from django.contrib import admin
from .models import Redaccion, Category, Comentario
# Register your models here.
admin.site.register(Redaccion)
admin.site.register(Category)
admin.site.register(Comentario)