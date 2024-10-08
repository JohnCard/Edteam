from django.db import models
from Coursera.models import User
# Create your models here.

class Youtuber(User):
    # background image
    background = models.TextField(verbose_name='De que tratará tu canal', default='Contenido publico', null=False, blank=False)

class Video(models.Model):
    # title
    title = models.CharField(verbose_name='Titulo', max_length=35, null=False, blank=False, unique=True)
    # date
    date = models.DateField(auto_now_add=True)
    # description
    description = models.TextField(verbose_name='Descripcción', default='Nuevo contenido', null=True, blank=True)
    # background image
    img = models.ImageField(verbose_name='Imagen de fondo', default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/2048px-Python.svg.png', null=True, blank=True)
    # youtuber
    youtuber = models.ForeignKey(Youtuber, on_delete=models.CASCADE, verbose_name='Youtuber', null=False)
    # views
    views = models.IntegerField(null=True, blank=True) 