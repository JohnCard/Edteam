from rest_framework import serializers
from rest_framework.serializers import CharField, ValidationError, ModelSerializer
from .models import Course, Teacher, Vehicle,Alumn
from rest_framework.response import Response

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','title', 'qualification','img','modules','teacher','description','price')
        read_only_fields = ('date', )
        
class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id','owner', 'plaque', 'vin', 'brand','sub_brand','verify_reason','service','line','no_tech','folio')
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','name','age','experience','courses')
        
class Url(ModelSerializer):
    class Meta:
        model = Alumn
        fields = ['name','url']
    def ret(self):
        nam = self.validated_data['name']
        ur = self.validated_data["url"]
        alumno = Alumn(name=nam,url=ur)
        alumno.save()
        return alumno
class Alumn(serializers.Serializer):
    name = serializers.CharField(max_length=15)