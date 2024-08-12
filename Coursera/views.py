from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.http.response import JsonResponse
from django.views import View
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from .forms import CourseForm, formCourse
from .models import Course, Teacher
from .mixins import TitleMixin, LinkMixin, StyleMix
from .serializers import CourseSerializer, TeacherSerializerSec
from .pagination import CourseCPagination

# Create your views here.

class TeacherView(viewsets.ModelViewSet):
    # queryset
    queryset = Teacher.objects.all()
    # serializer class
    serializer_class = TeacherSerializerSec

class PaginationView(generics.ListAPIView):
    # queryset
    queryset = Course.objects.all()
    # serializer class
    serializer_class = CourseSerializer
    # pagination class
    pagination_class = CourseCPagination
    # permission classes
    permission_classes = [
        IsAuthenticated
    ]

class CourseView(View):
    def get(self, id=0):
        #? ¿got an id?, we retrieve an specific course by it´s pk
        if (id > 0):
            # get course info
            course = list(Course.objects.filter(id=id).values())
            if len(course) > 0:
                company = course[0]
                datos = {'message': "Success", 'company': company}
            #! ¡course not found
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
        # pull all courses data
        courses = list(Course.objects.values())
        if len(courses) > 0:
            datos = {'message': "Success", 'courses': courses}
        #! ¡empty data!
        datos = {'message': "courses not found..."}
        return JsonResponse(datos)

    def post(self, request):
        # pull request data
        jd = json.loads(request.body)
        # create course
        Course.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        # return succes message
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        #? ¿well done?
        try:
            # pull request data
            jd = json.loads(request.body)
            # get specific course
            company = Course.objects.get(id=id)
            # updating course instance
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            # save new instance
            company.save()
            # response message
            data = {'message': "Success"}
        #! ¡something went wrong!
        except:
            # response message
            data = {'message': "Company not found..."}
        finally:
            return JsonResponse(data)
    
    def delete(self, id):
        #? ¿well done?
        try:
            # delete instance
            Course.objects.filter(id=id).delete()
            # prepare response
            datos = {'message': "Success"}
        #! ¡something went wrong!
        except:
            # prepare response
            datos = {'message': "Company not found..."}
        finally:
            return JsonResponse(datos)

class CourseNewApi(APIView):
    def get(self, id=None):
        #? ¿got an id?
        if id is not None:
            # get course
            course = Course.objects.get(id=id)
            # serialize data
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        # get all courses
        courses = Course.objects.all()
        # serialize data
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        # serialize data
        serializer = CourseSerializer(data=request.data)
        #? ¿valid data?
        if serializer.is_valid():
            # save instance
            serializer.save()
            return Response({'ok': True}, status=status.HTTP_201_CREATED)
        #! ¡bad request! 
        return Response({'ok': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        # get course
        course = Course.objects.get(id=id)
        # get serialized data
        serializer = CourseSerializer(course, data=request.data)
        #? ¿valid data?
        if serializer.is_valid():
            # save data
            serializer.save()
            return Response({'ok': True}, status=status.HTTP_201_CREATED)
        #! ¡something went wrong!
        return Response({'ok': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        # get course
        course = Course.objects.get(id=id)
        # serialize data
        serializer = CourseSerializer(course, data=request.data, partial=True)
        #? ¿valid data? 
        if serializer.is_valid():
            # partial save
            serializer.save()
            return Response({'Method':'Well partial done ;)'})
        #! ¡something went wrong! 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, id):
        # get course
        course = Course.objects.get(pk=id)
        # delete instance
        course.delete()
        return Response({'msg': 'Deleted correctly'})    

class CourseApis(viewsets.ModelViewSet):
    # define serializer class
    serializer_class = CourseSerializer
    # get queryset
    def get_queryset(self):
        courses = Course.objects.all()
        return courses
    
    def list(self):
        # get all courses
        courses = CourseSerializer(self.get_queryset(),many=True)
        return Response(courses.data)
            
    def retrieve(self, **kwargs):
        #? ¿does this course exist?
        try: 
            # filter course by id/pk
            projects = Course.objects.filter(id=kwargs['pk'])
            # serialize data
            serializer = CourseSerializer(projects,many=True)
            return Response(serializer.data)
        #! ¡does not exist! 
        except:
            return Response({'Message': 'We couldn´t ubicate this item'})
    
    def create(self, request):
        # pull data
        data = request.data
        # create instance (course)
        new_course = Course.objects.create(title=data['title'], qualification=data['qualification'],img=data['img'], modules=data['modules'], teacher=data['teacher'], description=data['description'], price=data['price'])
        # save new instance
        new_course.save()
        # serialize data
        serializer = CourseSerializer(new_course)
        return Response(serializer.data)
    
    def destroy(self):
        #? ¿well done?
        try:
            # get id
            id = self.kwargs["pk"]
            # get instance
            commit = get_object_or_404(Course, id=id)
            # delete instance
            commit.delete()
            return Response({'Message': 'Object deleted successfully'})
        except:
            return Response({'Message':'we couldn´t get the item indicated'})
    
    def update(self, request):
        # try to extract instance or an 404 error
        course = get_object_or_404(Course, id=self.kwargs["pk"])
        # serialize data
        course_serializer = CourseSerializer(course, data=request.data)
        #? ¿valid data?
        if course_serializer.is_valid():
            # save new data
            course_serializer.save()
            return Response(course_serializer.data)
        return Response({'Message': 'Failed request'})
    
    def partial_update(self, request):
        # try to pull instance or an 404 error
        course = get_object_or_404(Course, id=self.kwargs["pk"])
        # serialize data
        serializer = CourseSerializer(course, data=request.data, partial=True)
        #? ¿valida data?
        if serializer.is_valid():
            return Response(request.data)
        return Response("wrong parameters")   

def list(request):
    # get request data
    query = request.GET.get('q', None)
    # get all courses
    queryset = Course.objects.all()
    #? ¿valid data?
    if query is not None:
        # filter instance
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query) |
            Q(qualification__icontains=query) |
            Q(date__icontains=query) |
            Q(teacher__icontains=query)
        )
    # build context
    context = {
        'Courses': queryset
    }
    return render(request, 'List.html',context)

def form(request):
    # get form
    form = CourseForm(request.POST or None)
    #? ¿valid data? 
    if form.is_valid():
        # save data
        instance = form.save(commit=False)
        instance.save()
        # redirect to new course instance
        return HttpResponseRedirect(f'/Detail/{instance.id}')
    # build context
    context = {
        'form': form
    }
    return render(request, 'Form.html',context)

def detail(request,id_course):
    # bring course/instance or an 404 error
    instance = get_object_or_404(Course,id=id_course)
    # build context
    context = {
        'course': instance
    }
    return render(request, 'Detail.html',context)

def update(request,id_course):
    # get course/instance or 404 error
    instance = get_object_or_404(Course, id=id_course)
    # get course form
    form = CourseForm(request.POST or None, instance=instance)
    #? ¿valid data? 
    if form.is_valid():
        # save changes
        instance = form.save(commit=False)
        instance.save()
        # redirect to new changes
        return HttpResponseRedirect(f'/Detail/{instance.id}')
    # build context
    context = {
        'form': form,
        'course': instance
    }
    return render(request, 'Update.html', context)

def delete(request, id_course):
    # get course/instance or 404 error
    instance = get_object_or_404(Course, id=id_course)
    #? ¿requested method?
    if request.method == 'POST':
        # delete course
        instance.delete()
        # redirect to main page
        return HttpResponseRedirect('/Courses/')
    # build context
    context = {
        'course': instance 
    }
    return render(request, 'Delete.html',context)

class DeleteCourse(DeleteView):
    # define mode
    model = Course
    # define template
    template_name = 'pages/Delete.html'
    
    # define queryset
    def get_queryset(self):
        # pull id
        course_id = self.kwargs.get('pk')  
        # filter instance
        queryset = Course.objects.filter(pk=course_id)
        return queryset
    
    # succesfull operation
    def get_success_url(self):
        return '/allCourses/'

class CoursesView(TitleMixin, ListView):
    # define mode
    model = Course
    # template title
    title = 'Edteam courses'
    # define template
    template_name = 'pages/List.html' 
    
    # define queryset
    def get_queryset(self):
        return Course.objects.all()
    
class CreateView(CreateView, LinkMixin, StyleMix, ListView): 
    # define class form
    form_class = CourseForm
    # define class template
    template_name = 'pages/Form.html'
    # get link
    link = '/allCourses/'
    # define stylesheet
    stylesheet = 'Form2.css'
    
    # define queryset
    def get_queryset(self):
        return Course.objects.all()
    
    #? ¿valid data?
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponseRedirect('/allCourses/')
    
    #! ¡something went wrong! 
    def form_invalid(self,form):
        return super().form_invalid(form)
    
class DetailView(DetailView):
    # define model
    model = Course 
    # define template class
    template_name = 'pages/Detail.html' 
    
    # define queryset
    def get_queryset(self):
        # pull id
        course_id = self.kwargs.get('pk')  
        # filter course/instance
        queryset = Course.objects.filter(pk=course_id)
        return queryset
    
class UpdateView(UpdateView):
    # define form class
    form_class = formCourse
    # define template class
    template_name = 'pages/Detail.html'
    
    # define queryset
    def get_queryset(self):
        return Course.objects.filter(id=self.kwargs.get('pk'))
    
    #? ¿valid data?
    def get_success_url(self):
        self.object.get_edit_url()
        return '/allCourses/'
