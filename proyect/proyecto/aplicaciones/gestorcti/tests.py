from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import *
from .serializer import UsuarioSerializer
from rest_framework import serializers

class UsuarioArticuloViewsetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Creación de instancias en el modelo Usuario
        self.user1 = Usuario.objects.create(
            nombre='Yanne',
            nombreUsuario='yane1',
            apellidos='Liriano',
            nivel=5,
            correo='yn@example.com',
        )
        self.user2 = Usuario.objects.create(
            nombre='Charly',
            nombreUsuario='charl1',
            apellidos='Liriano',
            nivel=5,
            correo='charly@example.com',
        )

    def test_get_users_by_name(self):
        # Filtrar usuarios por nombre 'Yanne'
        response = self.client.get('http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=yane1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar que solo se devuelve el usuario 'Yanne'
        serializer = UsuarioSerializer(self.user1)
        expected_data = {
            'id': self.user1.id,
            'nombre': 'Yanne',
            'nombreUsuario': 'yane1',
            'apellidos': 'Liriano',
            'nivel': 5,
            'correo': 'yn@example.com',
            'departamento': None  # Reemplaza con el ID del departamento si se ha asignado
        }
        self.assertEqual(response.data, [expected_data])
    def test_get_users_by_non_existing_name(self):
        # Buscar un usuario que no exista, utilizando un nombre inexistente
        response = self.client.get('http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=Karina')
        # Verificar que se recibe un código de estado 200 como q no encontro ese usuario
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verificar que la respuesta esté vacía (en caso de no haber datos)
        self.assertEqual(response.data, [])

# Create your tests here.
