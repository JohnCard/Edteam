from django.db import models

# Create your models here. 
    
class User(models.Model):
    name = models.CharField(max_length=35, verbose_name='Nombre', null=False, blank=False)
    birthday = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    url = models.SlugField(max_length=15, verbose_name='Url de usuario', null=True, blank=True)
    
    class Meta:
        abstract = True

class Teacher(User):
    experience = models.IntegerField(verbose_name='Años de experiencia', null=False, blank=False)  

class Course(models.Model):
    title = models.CharField(max_length=20, verbose_name='Titulo del curso', null=False, blank=False, unique=True)
    qualification = models.IntegerField(default=8, verbose_name='Calificación', null=True, blank=True)
    img = models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png', verbose_name='Imagen de fondo', null=True, blank=True)
    modules = models.IntegerField(verbose_name='Cantidad de modulos', default=5, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Profesor del curso', null=False)
    description = models.TextField(verbose_name='Descripcción', default='A good course', null=True, blank=True)
    price = models.IntegerField(verbose_name='Precio del curso', default=400, null=True, blank=True)
    
    def get_absolute_url(self):
        return f'/detailCourse/{self.id}'
    
    def get_edit_url(self):
        return f'/updateCourse/{self.id}'
    
    def get_delete_url(self):
        return f'/updateCourse/{self.id}/delete'

class Vehicle(models.Model):
    owner = models.CharField(max_length=35)
    plaque = models.CharField(max_length=20)
    vin = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    sub_brand = models.CharField(max_length=20)
    verify_reason = models.CharField(max_length=30)
    service = models.CharField(max_length=15)
    line = models.IntegerField()
    no_tech = models.IntegerField()
    folio = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
class Alumn(User):
    score = models.IntegerField(verbose_name='Promedio del alumno', null=True, blank=True)
