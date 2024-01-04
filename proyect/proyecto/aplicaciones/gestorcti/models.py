from django.db import models

# Create your models here.

class Facultad(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.nombre
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self) :
        return self.nombre

############## ACTOR ######################################################################################
class Usuario(models.Model):
    nombre = models.CharField(max_length=20,blank=True)
    nombreUsuario =models.CharField(max_length=20,blank=True)
    apellidos = models.CharField(max_length=30,blank=True)
    nivel = models.IntegerField(blank=True)
    correo = models.EmailField(blank=True ,null=True)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.nombre
    
############## PUBLICACIONES ##########################################################################
class Publicacion(models.Model):
    titulo = models.CharField(max_length=500,blank=True)
    autores = models.ManyToManyField(Usuario,blank=True)
    ano = models.IntegerField(blank=True)
    pais = models.CharField(max_length=30, blank=True)
    formato = models.BooleanField(default=1,blank=True)
    link = models.URLField(blank=True)
    area = models.CharField( max_length=50,blank=True)
    estado = models.CharField(max_length=15 ,blank=True , null=True)
    def __str__(self):
        return self.titulo
    class Meta:
        abstract = True

class Articulo (Publicacion):
    issn = models.CharField(max_length=10,blank=True)
    paginas = models.CharField(max_length= 30,blank=True)
    titulo_revista = models.CharField(max_length=200,blank=True)
    volumen = models.CharField(max_length=30,blank=True)
    bd_referenciada = models.CharField(max_length=30,blank=True)
    area_conocimiento = models.CharField( max_length=200,blank=True)
    factor_impacto = models.CharField(max_length= 200,blank=True)
    

class Libro (Publicacion):
    editorial = models.CharField(max_length=500,blank=True)
    paginas = models.IntegerField(blank=True)
    isbn = models.CharField(max_length=200,blank=True)

class Monografia (Publicacion):
    editorial = models.CharField(max_length=500)
    paginas = models.IntegerField()
    isbn = models.CharField(max_length=200)

################CONDECORACIONES##########################################################################
class Condecoracion(models.Model):
    autores = models.ManyToManyField(Usuario,blank=True)
    alcance = models.CharField(max_length=50, blank=True)
    otorgado_por = models.CharField(max_length=200,blank=True)
    fecha = models.DateField(blank=True, null=True)
    pais = models.CharField(max_length=50 , blank=True)
    estado = models.CharField(max_length=15 ,blank=True , null=True)
    class Meta :
        abstract = True

class Premio(Condecoracion):
    denominacion = models.CharField(max_length=200,blank=True)
    titulo_resultado = models.CharField(max_length=500,blank=True)
    sector_estrategico = models.CharField(max_length=200,blank=True)
    nombre_evento = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.denominacion
    
class Reconocimiento (Condecoracion):
    nombre_reconocimiento = models.CharField(max_length=200,blank=True)
    causa = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.nombre_reconocimiento
    