from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.TextField()
    date = models.DateField(auto_now_add=True)
    during = models.IntegerField(default=5)
    description = models.CharField(default='Enjoy the content from this tube ;)!.', max_length=200)
    img = models.ImageField(default='https://i.blogs.es/9b19ad/youtube/1366_2000.jpg')
    icon = models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png')
    youtuber = models.CharField(max_length=70,default='Developer avenger')
    views = models.PositiveBigIntegerField(default=10000)
    
class Youtuber(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    topyc = models.CharField(max_length=100)
    
    