from rest_framework import serializers
from .models import Course, Teacher

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','title', 'qualification','img','modules','teacher','description','price')
        read_only_fields = ('date', )
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','name','age','experience','courses')
        
class Alumn(serializers.Serializer):
    name = serializers.CharField(max_length=15)