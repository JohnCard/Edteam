from django.shortcuts import render, get_object_or_404
from .forms import CourseForm,formCourse
from django.http import HttpResponseRedirect
from .models import Course,Vehicle
from django.db.models import Q
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView
from .mixins import TitleMixin, linkMixin,styleMix
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import viewsets,status,generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CourseSerializer,Alumn, vehicleSerializer, Url
from .pagination import CoursePagination,CourseCPagination
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View
# import requests
# from bs4 import BeautifulSoup
from .tests import get_data
from datetime import datetime, timedelta
import json
# Create your views here.

def schedule_dates(long, time_init='07:00', time_finish='23:30'):
    
    # Init and finish times
    hora_inicio = datetime.strptime(time_init, "%H:%M")
    hora_fin = datetime.strptime(time_finish, "%H:%M")
    
    # Assigning interval list
    lista_intervalos = []
    
    # Generating interval list
    while hora_inicio < hora_fin:
        # Adding finish time for actual interval
        intervalo_fin = hora_inicio + timedelta(minutes=long)
        
        # Adjusting last interval for finish time
        if intervalo_fin > hora_fin:
            intervalo_fin = hora_fin
        
        # Adding last interval for list in "HH:MM-HH:MM" format
        lista_intervalos.append(f"{hora_inicio.strftime('%H:%M')}-{intervalo_fin.strftime('%H:%M')}")
        
        # Continue next interval
        hora_inicio = intervalo_fin
    
    return lista_intervalos    

# class DoctorSchedules(GenericAPIView):
#     """
#         Get all schedules for one specific doctor

#         Args:
#             GenericAPIView (class): Base class for all other generic views.

#         Returns:
#             [GET] Response: A doctor´s schedules data with HTTP 201 if ok or 400 status if any error
#     """
#     def get(self, request, *args, **kwargs):
        
#         # Make a respon dictionary to build a response if the view runs successfully or fails
#         respon = {}
        
#         #? Well done?
#         try:
#             ###* Get data -> Extracting all data we need to add to response as data parameter for respon dictionary
#             doctor = self.request.query_params
#             doctor = doctor.get('id')
#             doctor = int(doctor)
#             dates = list(ConsultationSchedule.objects.filter(doctor=doctor))
#             dates = map(lambda e:{'id':e.pk,'doctor':e.doctor.name,'date':e.date,'hours':json.loads(e.hours)['hours'], 'status': e.status,'patients':map(lambda e:e.name,list(e.patients.all()))},dates)
#             ###* Get data
            
#             ### Prepare your dictionary that will be sent as a response
#             respon['ok'] = True
#             respon['data'] = dates
            
#             #* Returning data
#             return response.Response(respon, status=status.HTTP_201_CREATED)
#         #! Something went wrong
#         except Exception as e:
#             ### Building dictionary
#             respon['ok'] = False
#             respon['error'] = str(e)
#             ### Building dictionary
            
#             #* Return 400 response
#             return response.Response(respon, status=status.HTTP_400_BAD_REQUEST)

# class ConsultationScheduleGenerator(GenericAPIView):
#     """
#         Post view generator for new ConsultationSchedule instances

#         Args:
#             GenericAPIView (class): Base class for all other generic views.

#         Returns:
#             [POST] Response: ConsultationSchedule's serialized data with HTTP 201 if ok or 400 status if any error
#     """
#     # Define none authentication required for this class
#     authentication_classes = []
#     #* Define serializer class
#     serializer_class = acc_ser.ConsultantSerializerGeneric
    
#     def post(self, request):
#         #* This "try" estructure will extract all data we need to start
#         try:
#             duration = request.data['duration']
#             date_start = datetime.strptime(request.data['date_start'], '%d/%m/%Y')
#             date_finish = datetime.strptime(request.data['date_finish'], '%d/%m/%Y')
#             doctor_id = request.data['doctor']
#             #* We get the doctor instance using the doctor_id parameter we got extracting data from request data
#             doctor = Doctor.objects.all().get(id=doctor_id)
#         #! Something went wrong with data
#         except Exception as e:
#             return response.Response({'error': f'Error al obtener alguno de los datos: {e}.'}, status=status.HTTP_400_BAD_REQUEST)
                
#         #? Is duration parameter correct?
#         if duration != 15 and duration != 30 and duration != 45:
#             return response.Response({'error': 'Formato de duración no aceptado.'}, status=status.HTTP_400_BAD_REQUEST)
#         elif date_start >= date_finish:
#             return response.Response({'error': 'Por favor, verifique sus fechas.'}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Make a respon variable dictionary parameter for good/bad case
#         respon = {}
#         # get schedules data
#         schedules = schedule_dates(duration)
        
#         ###* Creating new ConsultationSchedule instances -> Block code dedicated to create new instances for    ConsultationSchedule model according to date_start and date_finish parameters from request data
#         current_date = date_start
#         consult_dates = []
#         while current_date <= date_finish:
#             json_serializer = {}
#             json_serializer['doctor'] = doctor.pk
#             json_serializer['date'] = current_date.date().strftime('%Y-%m-%d')
#             new_schedules = map(lambda e: {'hour':e,'status':'free','patient':None},schedules)
#             json_serializer['hours'] = json.dumps({'hours': list(new_schedules)})
#             serializer = self.serializer_class(data=json_serializer) 
#             #? Well done?
#             if serializer.is_valid():
#                 #// Save serializer Commented for a while
#                 #// serializer.save()
#                 json_serializer['doctor'] = doctor.name
#                 json_serializer['hours'] = json.loads(json_serializer['hours'])['hours']
#                 json_serializer['date'] = current_date.date().strftime('%d/%m/%Y')
#                 consult_dates.append(json_serializer)
#                 current_date += timedelta(days=1)
#         ###* Creating new ConsultationSchedule instances
#             #! Something went wrong and the cycle was interrupted
#             else:
#                 ###* Prepare response
#                 respon['ok'] = False
#                 lista = ''
#                 for k,v in serializer.errors.items():
#                     lista += f'{v[0]} | '
#                 lista = lista[:-3]
#                 respon['error'] = lista
#                 ###* Prepare response
                
#                 #* Return 400 response
#                 return response.Response(respon, status=status.HTTP_400_BAD_REQUEST)
#         # The process was finished succesfully
#         respon['ok'] = True
#         respon['data'] = consult_dates
#         # Return 201 response
#         return response.Response(respon, status=status.HTTP_201_CREATED)

# class ConsultationScheduleGenerate(GenericAPIView):
#     """
#         ConsultationSchedule post view dedicated to return a list full of time schedules

#         Args:
#             GenericAPIView (class): Base class for all other generic views.

#         Returns:
#             [POST] Response: list of interval times for a doctor day with HTTP 201 if ok or 400 status if any error
#     """
#     # Define none authentication required for this class
#     authentication_classes = []
    
#     def post(self, request):
#         #? Looking for duration parameter from request data
#         try:
#             duration = request.data['duration']
#         #! Duration parameter wasn´t sent well
#         except Exception as e:
#             return response.Response({'error': f'Verifique bien sus datos por favor: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Declarate a response dictionary variable to be used on 200 or 400 response
#         respon = {}
        
#         #? Is duration parameter valid?
#         if duration != 15 and duration != 30 and duration != 45:
#             ###* Prepare 400 response
#             respon['ok'] = False
#             respon['error'] = 'La duración especificada no es válida'
#             ###* Prepare 400 response
            
#             #! Return 400 response
#             return response.Response(respon, status=status.HTTP_400_BAD_REQUEST)
#         # Yes, it does
#         else:
#             dates = schedule_dates(duration)
#             ###* Prepare main data
#             respon['ok'] = True
#             respon['data'] = dates
#             ###* Prepare main data
            
#             #* Return correct response
#             return response.Response(respon, status=status.HTTP_201_CREATED)

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
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

def schedule_dates(long, time_init='07:00', time_finish='23:30'):
    
    # Init and finish times
    hora_inicio = datetime.strptime(time_init, "%H:%M")
    hora_fin = datetime.strptime(time_finish, "%H:%M")
    
    # Assigning interval list
    lista_intervalos = []
    
    # Generating interval list
    while hora_inicio < hora_fin:
        # Adding finish time for actual interval
        intervalo_fin = hora_inicio + timedelta(minutes=long)
        
        # Adjusting last interval for finish time
        if intervalo_fin > hora_fin:
            intervalo_fin = hora_fin
        
        # Adding last interval for list in "HH:MM-HH:MM" format
        lista_intervalos.append(f"{hora_inicio.strftime('%H:%M')}-{intervalo_fin.strftime('%H:%M')}")
        
        # Continue next interval
        hora_inicio = intervalo_fin
    
    return lista_intervalos    

# class DoctorSchedules(GenericAPIView):
#     """
#         Get all schedules for one specific doctor

#         Args:
#             GenericAPIView (class): Base class for all other generic views.

#         Returns:
#             [GET] Response: A doctor´s schedules data with HTTP 201 if ok or 400 status if any error
#     """
#     def get(self, request, *args, **kwargs):
        
#         # Make a respon dictionary to build a response if the view runs successfully or fails
#         respon = {}
        
#         #? Well done?
#         try:
#             ###* Get data -> Extracting all data we need to add to response as data parameter for respon dictionary
#             doctor = self.request.query_params
#             doctor = doctor.get('id')
#             doctor = int(doctor)
#             dates = list(ConsultationSchedule.objects.filter(doctor=doctor))
#             dates = map(lambda e:{'id':e.pk,'doctor':e.doctor.name,'date':e.date,'hours':json.loads(e.hours)['hours'], 'status': e.status,'patients':map(lambda e:e.name,list(e.patients.all()))},dates)
#             ###* Get data
            
#             ### Prepare your dictionary that will be sent as a response
#             respon['ok'] = True
#             respon['data'] = dates
            
#             #* Returning data
#             return response.Response(respon, status=status.HTTP_201_CREATED)
#         #! Something went wrong
#         except Exception as e:
#             ### Building dictionary
#             respon['ok'] = False
#             respon['error'] = str(e)
#             ### Building dictionary
            
#             #* Return 400 response
#             return response.Response(respon, status=status.HTTP_400_BAD_REQUEST)

# class ConsultationScheduleGenerator(GenericAPIView):
#     """
#         Post view generator for new ConsultationSchedule instances

#         Args:
#             GenericAPIView (class): Base class for all other generic views.

#         Returns:
#             [POST] Response: ConsultationSchedule's serialized data with HTTP 201 if ok or 400 status if any error
#     """
#     # Define none authentication required for this class
#     authentication_classes = []
#     #* Define serializer class
#     serializer_class = acc_ser.ConsultantSerializerGeneric
    
#     def post(self, request):
#         #* This "try" estructure will extract all data we need to start
#         try:
#             duration = request.data['duration']
#             date_start = datetime.strptime(request.data['date_start'], '%d/%m/%Y')
#             date_finish = datetime.strptime(request.data['date_finish'], '%d/%m/%Y')
#             doctor_id = request.data['doctor']
#             #* We get the doctor instance using the doctor_id parameter we got extracting data from request data
#             doctor = Doctor.objects.all().get(id=doctor_id)
#         #! Something went wrong with data
#         except Exception as e:
#             return response.Response({'error': f'Error al obtener alguno de los datos: {e}.'}, status=status.HTTP_400_BAD_REQUEST)
                
#         #? Is duration parameter correct?
#         if duration != 15 and duration != 30 and duration != 45:
#             return response.Response({'error': 'Formato de duración no aceptado.'}, status=status.HTTP_400_BAD_REQUEST)
#         elif date_start >= date_finish:
#             return response.Response({'error': 'Por favor, verifique sus fechas.'}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Make a respon variable dictionary parameter for good/bad case
#         respon = {}
#         # get schedules data
#         schedules = schedule_dates(duration)
        
#         ###* Creating new ConsultationSchedule instances -> Block code dedicated to create new instances for    ConsultationSchedule model according to date_start and date_finish parameters from request data
#         current_date = date_start
#         consult_dates = []
#         while current_date <= date_finish:
#             json_serializer = {}
#             json_serializer['doctor'] = doctor.pk
#             json_serializer['date'] = current_date.date().strftime('%Y-%m-%d')
#             new_schedules = map(lambda e: {'hour':e,'status':'free','patient':None},schedules)
#             json_serializer['hours'] = json.dumps({'hours': list(new_schedules)})
#             serializer = self.serializer_class(data=json_serializer) 
#             #? Well done?
#             if serializer.is_valid():
#                 #// Save serializer Commented for a while
#                 #// serializer.save()
#                 json_serializer['doctor'] = doctor.name
#                 json_serializer['hours'] = json.loads(json_serializer['hours'])['hours']
#                 json_serializer['date'] = current_date.date().strftime('%d/%m/%Y')
#                 consult_dates.append(json_serializer)
#                 current_date += timedelta(days=1)
#         ###* Creating new ConsultationSchedule instances
#             #! Something went wrong and the cycle was interrupted
#             else:
#                 ###* Prepare response
#                 respon['ok'] = False
#                 lista = ''
#                 for k,v in serializer.errors.items():
#                     lista += f'{v[0]} | '
#                 lista = lista[:-3]
#                 respon['error'] = lista
#                 ###* Prepare response
                
#                 #* Return 400 response
#                 return response.Response(respon, status=status.HTTP_400_BAD_REQUEST)
#         # The process was finished succesfully
#         respon['ok'] = True
#         respon['data'] = consult_dates
#         # Return 201 response
#         return response.Response(respon, status=status.HTTP_201_CREATED)

# class ConsultationScheduleGenerate(GenericAPIView):
#     """
#         ConsultationSchedule post view dedicated to return a list full of time schedules

#         Args:
#             GenericAPIView (class): Base class for all other generic views.

#         Returns:
#             [POST] Response: list of interval times for a doctor day with HTTP 201 if ok or 400 status if any error
#     """
#     # Define none authentication required for this class
#     authentication_classes = []
    
#     def post(self, request):
#         #? Looking for duration parameter from request data
#         try:
#             duration = request.data['duration']
#         #! Duration parameter wasn´t sent well
#         except Exception as e:
#             return response.Response({'error': f'Verifique bien sus datos por favor: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Declarate a response dictionary variable to be used on 200 or 400 response
#         respon = {}
        
#         #? Is duration parameter valid?
#         if duration != 15 and duration != 30 and duration != 45:
#             ###* Prepare 400 response
#             respon['ok'] = False
#             respon['error'] = 'La duración especificada no es válida'
#             ###* Prepare 400 response
            
#             #! Return 400 response
#             return response.Response(respon, status=status.HTTP_400_BAD_REQUEST)
#         # Yes, it does
#         else:
#             dates = schedule_dates(duration)
#             ###* Prepare main data
#             respon['ok'] = True
#             respon['data'] = dates
#             ###* Prepare main data
            
#             #* Return correct response
#             return response.Response(respon, status=status.HTTP_201_CREATED)
