from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
        
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveBigIntegerField(
        validators=[
            MinValueValidator(25),
            MaxValueValidator(90)
        ]
    )
    experience = models.PositiveIntegerField()
    courses = models.TextField()
        
OPTIONS = [
    ('opt 1','Álvaro Felipe'),
    ('opt 2','Beto Quiroga'),
    ('opt 3','Alexys Lozada'),
    ('opt 4','Johnny'),
    ('opt 5','Queta Rodriguez'),
    ('opt 6','Oscar Alzada')
] 
        
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    qualification = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        default=7
    )
    img = models.ImageField(default='https://assets-global.website-files.com/6410ebf8e483b5bb2c86eb27/6410ebf8e483b53d6186fc53_ABM%20College%20Web%20developer%20main.jpg')
    date = models.DateField(auto_now_add=True)
    modules = models.PositiveSmallIntegerField(default=5,
                                               validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ])
    teacher = models.CharField(max_length=30,choices=OPTIONS,default='Álvaro Felipe')
    description = models.TextField(default='A good course to learning this technology')
    price = models.PositiveSmallIntegerField(default=400)
    
    def get_absolute_url(self):
        return f'/detailCourse/{self.id}'
    
    def get_edit_url(self):
        return f'/updateCourse/{self.id}'
    
    def get_delete_url(self):
        return f'/updateCourse/{self.id}/delete'
