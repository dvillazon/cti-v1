
from django_filters import rest_framework as filters
from .models import Articulo,Usuario

class ArticuloFilter(filters.FilterSet):
    autores = filters.ModelMultipleChoiceFilter(
        field_name ='autores__Articulo',
        to_field_name = 'id',
        queryset =Usuario.objects.all()
    )
    class Meta:
        model = Articulo
        fields = ['autores__id__Articulo']
