from django.shortcuts import render, get_object_or_404
from .forms import CourseForm,formCourse
from django.http import HttpResponseRedirect
from .models import Course, Vehicle, Teacher
from django.db.models import Q
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView
from .mixins import TitleMixin, linkMixin,styleMix
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import viewsets,status,generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CourseSerializer,Alumn, vehicleSerializer, Url, TeacherSerializerSec
from .pagination import CoursePagination,CourseCPagination
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View
# import requests
# from bs4 import BeautifulSoup
from .tests import get_data
# Create your views here.

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializerSec

class Methods(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            url = request.data['url']
            response = get_data(url)
            return Response({'ok':True,'data':response})
        except Exception as e:
            return Response({'ok':False,'error':str(e)})

class PaginationView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CourseCPagination
    permission_classes = [
        IsAuthenticated
    ]
    
class PaginationViewVehicle(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = vehicleSerializer
    pagination_class = CourseCPagination
    permission_classes = [
        IsAuthenticated
    ]

class CourseView(View):

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            course = list(Course.objects.filter(id=id).values())
            if len(course) > 0:
                company = course[0]
                datos = {'message': "Success", 'company': company}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
        else:
            courses = list(Course.objects.values())
            if len(courses) > 0:
                datos = {'message': "Success", 'courses': courses}
            else:
                datos = {'message': "courses not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Course.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Course.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Course.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        course = list(Course.objects.filter(id=id).values())
        if len(course) > 0:
            Course.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

class NewApi(APIView):
    
    def get(self,request,id=None, format=None):
        # courses = Course.objects.all()
        # serializer = CourseSerializer(courses, many=True)
        # return Response(serializer.data)
        id = id
        if id is not None:
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # serializer = self.serializer_class(data=request.data)
        # serializer = CourseSerializer(data=request.data) 
        # if serializer.is_valid():
        #     # name = serializer.validated_data.get("name")
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Well done'}, status=status.HTTP_201_CREATED)
        return Response({'ok': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id, format=None):
        
        id = id
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Method':'Well done ;)'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,id=None):
        id = id
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Method':'Well partial done ;)'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        id = id
        course = Course.objects.get(pk=id)
        course.delete()
        return Response({'msg': 'Deleted correctly'})    

class CourseApis(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        courses = Course.objects.all()
        return courses
    
    def list(self, request, *args, **kwargs):
        courses = CourseSerializer(self.get_queryset(),many=True)
        return Response(courses.data)
            
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

# def list(request):
#     query = request.GET.get('q',None)
#     queryset = Course.objects.all()
#     if query is not None:
#         queryset = queryset.filter(
#             Q(title__icontains=query) |
#             Q(price__icontains=query) |
#             Q(description__icontains=query) |
#             Q(qualification__icontains=query) |
#             Q(date__icontains=query) |
#             Q(teacher__icontains=query)
#         )
#     context = {
#         'Courses': queryset
#     }
#     return render(request, 'List.html',context)

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
