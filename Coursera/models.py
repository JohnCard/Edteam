from django.db import models

# Create your models here. 
    
class User(models.Model):
    # username
    name = models.CharField(max_length=35, verbose_name='Nombre', null=False, blank=False)
    # birthday
    birthday = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    # url
    url = models.SlugField(max_length=15, verbose_name='Url de usuario', null=True, blank=True)
    
    class Meta:
        abstract = True

class Teacher(User):
    # experience based on years
    experience = models.IntegerField(verbose_name='Años de experiencia', null=False, blank=False)  
class Course(models.Model):
    # course title
    title = models.CharField(max_length=20, verbose_name='Titulo del curso', null=False, blank=False, unique=True)
    # qualification comunity
    qualification = models.IntegerField(default=8, verbose_name='Calificación', null=True, blank=True)
    # background image
    img = models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png', verbose_name='Imagen de fondo', null=True, blank=True)
    # modules amount
    modules = models.IntegerField(verbose_name='Cantidad de modulos', default=5, null=True, blank=True)
    # teacher
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Profesor del curso', null=False)
    # description
    description = models.TextField(verbose_name='Descripcción', default='A good course', null=True, blank=True)
    # price
    price = models.IntegerField(verbose_name='Precio del curso', default=400, null=True, blank=True)
    
    def get_absolute_url(self):
        return f'/detail-course/{self.id}'
    
    def get_edit_url(self):
        return f'/update-course/{self.id}'
    
    def get_delete_url(self):
        return f'/update-course/{self.id}/delete'
    
class Alumn(User):
    # score
    score = models.IntegerField(verbose_name='Promedio del alumno', null=True, blank=True)
