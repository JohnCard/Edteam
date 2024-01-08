from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','title', 'qualification','img','modules','teacher','description','price')
        read_only_fields = ('date', )