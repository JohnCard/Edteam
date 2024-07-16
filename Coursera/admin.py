from django.contrib import admin
from .models import Course,Teacher,Vehicle,Alumn
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'qualification', 'modules', 'price')
    search_fields = ('id', 'title')
    ordering = ['id', 'title']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', )
    ordering = ['id', ]
    

# admin.site.register(Course, CourseAdmin)
# admin.site.register(Teacher)
# admin.site.register(Alumn)
# admin.site.register(Vehicle)

