from django import forms
from .models import Course
from .functions import cleanText

class CourseForm(forms.ModelForm):
    class Meta:
        labels = {
            'title':'Enter the course title',
            'qualification': 'Enter your expectative',
            'img': 'Enter an image',
            'teacher': 'Enter who will lead this course',
            'description':'Tell me about this course',
            'price': 'How much will you ask for it'
        }
        model = Course
        fields = [
        'title',
        'qualification',
        'img',
        'teacher',
        'description',
        'price']
        exclude = []
        
    def clean_title(self, *args, **kwargs):
        text = self.cleaned_data.get('title')
        if cleanText(text)>0:
            raise forms.ValidationError('Algo anda mal con el titulo del curso!!!')
        return text
    
    def clean_qualification(self,*args,**kwargs):
        num = self.cleaned_data.get('qualification')
        if num > 10:
            raise forms.ValidationError('El dato en especifico debe rondar entre 0-10!!!')
        return num
    
    def clean_price(self,*args, **kwargs):
        num = self.cleaned_data.get('price')
        if num < 80 or num > 1200:
            raise forms.ValidationError('Dato incorrecto, vuelva a intentarlo por favor!!!')
        return num

class formCourse(forms.ModelForm):
    class Meta:
        labels = {
            'title':'Enter the course title',
            'qualification': 'Enter your expectative',
            'img': 'Enter an image',
            'teacher': 'Enter who will lead this course',
            'description':'Tell me about this course',
            'price': 'How much will you ask for it'
        }
        model = Course
        fields = [
        'title',
        'qualification',
        'img',
        'teacher',
        'description',
        'price']
        exclude = []
        
    def clean_title(self, *args, **kwargs):
        text = self.cleaned_data.get('title')
        if cleanText(text)>0:
            raise forms.ValidationError('Algo anda mal con el titulo del curso!!!')
        return text
    
    def clean_qualification(self,*args,**kwargs):
        num = self.cleaned_data.get('qualification')
        if num > 10:
            raise forms.ValidationError('El dato en especifico debe rondar entre 0-10!!!')
        return num
    
    def clean_price(self,*args, **kwargs):
        num = self.cleaned_data.get('price')
        if num < 80 or num > 1200:
            raise forms.ValidationError('Dato incorrecto, vuelva a intentarlo por favor!!!')
        return num
    