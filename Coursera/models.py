from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here. 
    
class User(models.Model):
    name = models.CharField(max_length=30)
    # birthday = models.DateField(null=True, blank=True)
    url = models.SlugField(max_length=40, null=True)
    # created = models.DateTimeField(default=timezone.now().date().strftime('%Y-%m-%d'))
    # updated_at = models.DateTimeField(default=timezone.now().date().strftime('%Y-%m-%d'))
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

class Teacher(User):
    experience = models.IntegerField()  
          
class Course(models.Model):
    title = models.CharField(max_length=50)
    qualification = models.IntegerField(
        default=7
    )
    img = models.ImageField(default='https://assets-global.website-files.com/6410ebf8e483b5bb2c86eb27/6410ebf8e483b53d6186fc53_ABM%20College%20Web%20developer%20main.jpg')
    modules = models.IntegerField(default=5)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    description = models.TextField(default='A good course to learning this technology')
    price = models.IntegerField(default=400)
    # updated_at = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)
    
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
    score = models.IntegerField(null=True, blank=True)
