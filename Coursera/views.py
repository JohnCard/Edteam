from django.shortcuts import render, get_object_or_404
from .forms import CourseForm,formCourse
from django.http import HttpResponseRedirect
from .models import Course 
from django.db.models import Q
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView
from .mixins import TitleMixin, linkMixin,styleMix
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import viewsets
from .serializers import CourseSerializer
# Create your views here.

class CourseApi(APIView):
    serializer_class=CourseSerializer
    def get(self,request,id):
        try:
            return Response({'All our courses':Course.objects.filter(id=id).values()})
        except:
            projects = Course.objects.all().values()
            return Response({'Message':'List of projects','List':projects})

    def post(self, request):
        print('request: ',request.data)
        # serializer=CourseSerializer(data=request.data)
        # if(serializer.is_valid()):
        #     Course.objects.create(
        #     id=serializer.data.get('id'),
        #     title=serializer.data.get('title'),
        #     qualification=serializer.data.get('qualification'),
        #     img=serializer.data.get('img'),
        #     modules=serializer.data.get('modules'),
        #     teacher=serializer.data.get('teacher'),
        #     description=serializer.data.get('description'),
        #     price=serializer.data.get('price')
        #     )
        # course=Course.objects.all().filter(title=request.data['id']).values()
        # # return Response({'Message':'New Course added','Course':course})
        # return HttpResponseRedirect(f'/courseApi/{request.data["id"]}')
        
    def put(self, request):
        content={
            'Youre calling a put method'
        }
        return Response(content)

    def patch(self, request):
        content={
            'Youre calling a pacth method'
        }
        return Response(content)

    def delete(self, request):
        content ={
            'Youre calling a delete method'
        }
        return Response(content)
class CourseApis(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        courses = Course.objects.all()
        return courses
    
    def list(self, request, *args, **kwargs):
        projs_serializer = CourseSerializer(self.get_queryset(),many=True)
        return Response(projs_serializer.data)
            
    def retrieve(self, request, *args, **kwargs):
        try: 
            projects = Course.objects.filter(id=kwargs['pk'])
            serializer = CourseSerializer(projects,many=True)
            return Response(serializer.data)
        except:
            return Response({'Message': 'We couldn´t ubicate this item'})
    
    def create(self, request, *args, **kwargs):
        course_data = request.data
        new_course = Course.objects.create(title=course_data['title'],qualification=course_data['qualification'],img=course_data['img'],modules=course_data['modules'],teacher=course_data['teacher'],description=course_data['description'],price=course_data['price'])
        new_course.save()
        serializer = CourseSerializer(new_course)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        try:
            comment_id = self.kwargs["pk"]
            comment = get_object_or_404(Course, id=comment_id)
            comment.delete()
            return Response({'Message': 'Object deleted successfully'})
        except:
            return Response({'Message':'we couldn´t get the item indicated'})
    
    def update(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=self.kwargs["pk"])
        course_serializer = CourseSerializer(course, data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response({'Message': 'Failed request'})
    
    def partial_update(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=self.kwargs["pk"])
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(request.data)
        return Response("wrong parameters")   

def list(request):
    query = request.GET.get('q',None)
    queryset = Course.objects.all()
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query) |
            Q(qualification__icontains=query) |
            Q(date__icontains=query) |
            Q(teacher__icontains=query)
        )
    context = {
        'Courses': queryset
    }
    return render(request, 'List.html',context)

def form(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(f'/Detail/{instance.id}')
    context = {
        'form': form
    }
    return render(request, 'Form.html',context)

def detail(request,id_course):
    instance = get_object_or_404(Course,id=id_course)
    context = {
        'course': instance
    }
    return render(request, 'Detail.html',context)

def update(request,id_course):
    instance = get_object_or_404(Course, id=id_course)
    form = CourseForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(f'/Detail/{instance.id}')
    context = {
        'form': form,
        'course': instance
    }
    return render(request, 'Update.html', context)

def delete(request, id_course):
    instance = get_object_or_404(Course, id=id_course)
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect('/Courses/')
    context = {
        'course': instance 
    }
    return render(request, 'Delete.html',context)

class deleteCourse(DeleteView):
    model = Course
    template_name = 'pages/Delete.html'
    
    def get_queryset(self):
        course_id = self.kwargs.get('pk')  
        queryset = Course.objects.filter(pk=course_id)
        return queryset
    
    def get_success_url(self):
        return '/allCourses/'

class coursesView(TitleMixin,ListView):
    model = Course
    title = 'Edteam courses'
    template_name = 'pages/List.html' 
    
    def get_queryset(self):
        return Course.objects.all()
    
class createView(CreateView,linkMixin,styleMix,ListView): 
    form_class = CourseForm
    template_name = 'pages/Form.html'
    link = '/allCourses/'
    stylesheet = 'Form2.css'
    
    def get_queryset(self):
        return Course.objects.all()
    
    def form_valid(self,form):
        super().form_valid(form)
        return HttpResponseRedirect('/allCourses/')
    
    def form_invalid(self,form):
        return super().form_invalid(form)
    
class detailView(DetailView):
    model = Course
    template_name = 'pages/Detail.html'
    
    def get_queryset(self):
        course_id = self.kwargs.get('pk')  
        queryset = Course.objects.filter(pk=course_id)
        return queryset
    
class updateView(UpdateView):
    form_class = formCourse
    template_name = 'pages/Detail.html'
    
    def get_queryset(self):
        return Course.objects.filter(id=self.kwargs.get('pk'))
    
    def get_success_url(self):
        self.object.get_edit_url()
        return '/allCourses/'