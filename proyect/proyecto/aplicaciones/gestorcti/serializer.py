from rest_framework import serializers
from .models import Usuario
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta :
        model = Usuario
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta :
        model = Articulo
        fields = '__all__'
class LibroSerializer(serializers.ModelSerializer):
    class Meta :
        model = Libro
        fields = '__all__'
class MonografiaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Monografia
        fields = '__all__'
class PremioSerializer(serializers.ModelSerializer):
    class Meta :
        model = Premio
        fields = '__all__'        
class ReconocimientoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Reconocimiento
        fields = '__all__'        
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Departamento
        fields = '__all__'  
class FacultadSerializer(serializers.ModelSerializer):
    class Meta :
        model = Facultad
        fields = '__all__'  