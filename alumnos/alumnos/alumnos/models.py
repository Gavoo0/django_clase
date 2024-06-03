from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)

class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField()
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)

class Seccion(models.Model):
    id_seccion = models.AutoField(db_column='idSeccion',primary_key=True)
    seccion = models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return str(self.seccion)

class Ramo(models.Model):
    id_ramo = models.AutoField(db_column='idRamo',primary_key=True)
    ramo = models.CharField(max_length=200,null=False,blank=False)
    def __str__(self):
        return str(self.ramo)

class SeccionRamo(models.Model):
    id_SeccionRamo = models.AutoField(db_column='idSeccionRamo',primary_key=True)
    id_alumno = models.ForeignKey('Alumno',on_delete=models.CASCADE,db_column='idAlumno')
    id_seccion = models.ForeignKey('Seccion',on_delete=models.CASCADE,db_column='Seccion')
    def __str__(self):
        return str(self.id_alumno)