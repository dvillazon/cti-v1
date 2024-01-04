from django.contrib import admin
from .models import Usuario, Departamento, Facultad, Libro,Articulo,Monografia,Premio,Reconocimiento
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Departamento)
admin.site.register(Facultad)
admin.site.register(Articulo)
admin.site.register(Libro)
admin.site.register(Monografia)
admin.site.register(Premio)
admin.site.register(Reconocimiento)