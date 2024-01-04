from rest_framework.routers import DefaultRouter
from django.urls import path, include
from aplicaciones.gestorcti import viewsets
router = DefaultRouter()
router.register('usuario',viewsets.UsuarioArticuloViewset,basename="usuario")
router.register('articulo',viewsets.ArticuloViewset,basename="articulo")
router.register('libro',viewsets.LibroViewset,basename="libro")
router.register('monografia',viewsets.MonografiaViewset,basename="monografia")
router.register('premio',viewsets.PremioViewset,basename="premio")
router.register('reconocimiento',viewsets.ReconocimientoViewset,basename="reconocimiento")
router.register('departamento',viewsets.DepartamenViewset,basename="departamento")
router.register('facultad',viewsets.FacultadViewset,basename="facultad")
urlpatterns = [
    path('',include(router.urls))
]
