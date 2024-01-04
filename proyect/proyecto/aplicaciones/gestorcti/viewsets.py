from rest_framework import viewsets
from .models import Usuario, Articulo ,Libro
from .serializer import *
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import*

class UsuarioArticuloViewset(viewsets.ModelViewSet):
   # queryset=Usuario.objects.all()
    def get_queryset(self):
        queryset = Usuario.objects.all()
        nombreu = self.request.query_params.get('nombreUsuario', None)
        if nombreu:
            queryset = queryset.filter(nombreUsuario=nombreu)
        return queryset
    serializer_class = UsuarioSerializer
    ################# Articulos de un Usuario #############################################
    @action(detail=True)
    def write_articulo(self,request, *args, **kwargs):
        autor = self.get_object()
        articulo = autor.articulo_set.all()
        articulo_serial = ArticuloSerializer(articulo,many=True)
        return Response(articulo_serial.data)
        
    ######################### LIBRO de un Usuario#################################################
    @action(detail=True)
    def write_libro(self,request, *args, **kwargs):
        autor = self.get_object()
        libro = autor.libro_set.all()
        libro_serial = LibroSerializer(libro,many=True)
        return Response(libro_serial.data)
    ####################### Monografia de un Usuario #############################################
    @action(detail=True)
    def write_monografia(self,request, *args, **kwargs):
        autor = self.get_object()
        monografia = autor.monografia_set.all()
        monografia_serial = MonografiaSerializer(monografia,many=True)
        return Response(monografia_serial.data)
    ######################### Premio de un Usuario #############################################
    @action(detail=True)
    def write_premio(self,request, *args, **kwargs):
        autor = self.get_object()
        premio = autor.premio_set.all()
        premio_serial = PremioSerializer(premio,many=True)
        return Response(premio_serial.data)
    ################# Reconocimientos de un Usuario #############################################
    @action(detail=True)
    def write_reconocimiento(self,request, *args, **kwargs):
        autor = self.get_object()
        reconocimiento = autor.reconocimiento_set.all()
        reconocimiento_serial = ReconocimientoSerializer(reconocimiento,many=True)
        return Response(reconocimiento_serial.data)
    def perform_create(self, serializer):
        serializer.save()
    ##############################################################################
class ArticuloViewset(viewsets.ModelViewSet):
    queryset=Articulo.objects.all()
    serializer_class = ArticuloSerializer
    def perform_create(self, serializer):
        serializer.save()
class LibroViewset(viewsets.ModelViewSet):
    queryset=Libro.objects.all()
    serializer_class = LibroSerializer
    def perform_create(self, serializer):
        serializer.save()
class MonografiaViewset(viewsets.ModelViewSet):
    queryset=Monografia.objects.all()
    serializer_class = MonografiaSerializer
    def perform_create(self, serializer):
        serializer.save()
class PremioViewset(viewsets.ModelViewSet):
    queryset=Premio.objects.all()
    serializer_class = PremioSerializer
    def perform_create(self, serializer):
        serializer.save()
class ReconocimientoViewset(viewsets.ModelViewSet):
    queryset=Reconocimiento.objects.all()
    serializer_class = ReconocimientoSerializer
    def perform_create(self, serializer):
        serializer.save()

######################## En  departamentos #########################################
class DepartamenViewset(viewsets.ModelViewSet):
    queryset=Departamento.objects.all()
    serializer_class = DepartamentoSerializer

    @action(detail=True)
    def write_usuariod(self,request, *args, **kwargs): # USUARIOS DE UN DEPARTAMENTO
        departament = self.get_object()
        usuario = departament.usuario_set.all()
        usuario_serial = UsuarioSerializer(usuario,many=True)
        return Response(usuario_serial.data)
    
    @action(detail=True)
    def write_articulod(self,request, *args, **kwargs): # ARTICULOS DE UN DEPARTAMENTO
        departament = self.get_object()
        usuario = departament.usuario_set.all()
        alist = []
        for u in usuario:
            articulo = u.articulo_set.all()
            for a in articulo :
                alist.append(a)
        articulo_s = ArticuloSerializer(alist,many=True)
        return Response(articulo_s.data)
    
    @action(detail=True)
    def write_librod(self,request, *args, **kwargs): # LIBROS DE UN DEPARTAMENTO
        departament = self.get_object()
        usuario = departament.usuario_set.all()
        listl = []
        for u in usuario:
            libro = u.libro_set.all()
            for l in libro :
                listl.append(l)
        libro_s = LibroSerializer(listl,many=True)
        return Response(libro_s.data)
    
    @action(detail=True)
    def write_monografiad(self,request, *args, **kwargs): # MONOGRAFIA DE UN DEPARTAMENTO
        departament = self.get_object()
        usuario = departament.usuario_set.all()
        mlist = []
        for u in usuario:
            monografia = u.monografia_set.all()
            for m in monografia :
                mlist.append(m)
        monografia_s = MonografiaSerializer(mlist,many=True)
        return Response(monografia_s.data)

    @action(detail=True)
    def write_premiod(self,request, *args, **kwargs): # PREMIO DE UN DEPARTAMENTO
        departament = self.get_object()
        usuario = departament.usuario_set.all()
        plist = []
        for u in usuario:
            premio = u.premio_set.all()
            for p in premio :
                plist.append(p)
        premio_s = PremioSerializer(plist,many=True)
        return Response(premio_s.data)
    
    @action(detail=True)
    def write_reconocimientod(self,request, *args, **kwargs): # RECONOCIMIENTO DE UN DEPARTAMENTO
        departament = self.get_object()
        usuario = departament.usuario_set.all()
        rlist = []
        for u in usuario:
            reconocimiento = u.reconocimiento_set.all()
            for r in reconocimiento :
                rlist.append(r)
        reconocimiento_s = ReconocimientoSerializer(rlist,many=True)
        return Response(reconocimiento_s.data)
    
    def perform_create(self, serializer):
        serializer.save()

######################## En facultades ############################################
class FacultadViewset(viewsets.ModelViewSet):
    queryset=Facultad.objects.all()
    serializer_class = FacultadSerializer

    @action(detail=True)
    def write_userf(self,request, *args, **kwargs):############ USUARIO X FACULTAD
        facultad = self.get_object()  
        departamentos = facultad.departamento_set.all()
        ulist = []
        for d in departamentos:
            usuario = d.usuario_set.all()
            for u in usuario :
                ulist.append(u)
        usuario_s = UsuarioSerializer(ulist,many=True)
        return Response(usuario_s.data)
    
    @action(detail=True)
    def write_articulof(self,request, *args, **kwargs):########### ARTICULOS X FACULTAD
        facultad = self.get_object()  
        departamentos = facultad.departamento_set.all()
        ulist = []
        for d in departamentos:
            usuario = d.usuario_set.all()
            for u in usuario :
                articulo = u.articulo_set.all()
                for a in articulo:
                    ulist.append(a)
        articulo_s = ArticuloSerializer(ulist,many=True)
        return Response(articulo_s.data)
    
    @action(detail=True)
    def write_librof(self,request, *args, **kwargs):########### LIBROS X FACULTAD
        facultad = self.get_object()  
        departamentos = facultad.departamento_set.all()
        llist = []
        for d in departamentos:
            usuario = d.usuario_set.all()
            for u in usuario :
                libro = u.libro_set.all()
                for l in libro:
                    llist.append(l)
        libro_s = LibroSerializer(llist,many=True)
        return Response(libro_s.data)
    
    @action(detail=True)
    def write_monografiaf(self,request, *args, **kwargs):## MONOGRAFIA X FACULTAD
        facultad = self.get_object()  
        departamentos = facultad.departamento_set.all()
        mlist = []
        for d in departamentos:
            usuario = d.usuario_set.all()
            for u in usuario :
                monografia = u.monografia_set.all()
                for m in monografia:
                    mlist.append(m)
        monografia_s = MonografiaSerializer(mlist,many=True)
        return Response(monografia_s.data)
    
    @action(detail=True)
    def write_premiof(self,request, *args, **kwargs):## PREMIO X FACULTAD
        facultad = self.get_object()  
        departamentos = facultad.departamento_set.all()
        mlist = []
        for d in departamentos:
            usuario = d.usuario_set.all()
            for u in usuario :
                premio = u.premio_set.all()
                for p in premio:
                    mlist.append(p)
        premio_s = PremioSerializer(mlist,many=True)
        return Response(premio_s.data)

    @action(detail=True)
    def write_reconocimientof(self,request, *args, **kwargs):## RECONOCIMIENTO X FACULTAD
        facultad = self.get_object()  
        departamentos = facultad.departamento_set.all()
        mlist = []
        for d in departamentos:
            usuario = d.usuario_set.all()
            for u in usuario :
                reconocimiento = u.reconocimiento_set.all()
                for r in reconocimiento:
                    mlist.append(r)
        reconocimiento_s = ReconocimientoSerializer(mlist,many=True)
        return Response(reconocimiento_s.data)
    
    @action(detail=True, methods=['GET'])
    def dep_facultad(self, request, pk=None):
        facultad = self.get_object()  # Obtener la facultad por su clave primaria
        departamentos = Departamento.objects.filter(facultad=facultad)
        serializer = DepartamentoSerializer(departamentos, many=True)  # Reemplaza con tu serializer de Departamento
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save()
