import django_filters
from .models import Redaccion


class RedaccionFiltro(django_filters.FilterSet):

    class Meta:
        model = Redaccion
        fields = [  
            'categoria',
            'fecha',
        ]