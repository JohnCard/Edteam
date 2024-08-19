from django.urls import path, include
from rest_framework import routers
from .views import detail, form, update, delete, list, CoursesView, CreateView, DetailView, UpdateView, DeleteCourse, PaginationView, TeacherView, CourseGeneric, CourseAPIView, CourseRetrieveUpdateDestroyAPIView

router = routers.DefaultRouter()
# Define course api routers
router.register('course', CourseGeneric, basename='course')
router.register('teacher', TeacherView, basename='teacher')

urlpatterns = [
    path('', include(router.urls)),
    # Paginating all courses data
    path('pagination/',PaginationView.as_view(), name='pagination'),
    # Listening, creating, updating and deleteing courses
    path('course-view/', CourseAPIView.as_view(), name='course-view'),
    # retrieve course
    path('course-view/<int:id>', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-view'),
    # list all courses
    path('courses/', list),
    # retrieve a course data
    path('detail/<int:id_course>', detail),
    # create a new course
    path('form/', form),
    # update course
    path('update/<int:id_course>', update),
    # delete course
    path('delete/<int:id_course>', delete),
    # list all courses
    path('all-courses/', CoursesView.as_view()),
    # create a new course
    path('create-course/', CreateView.as_view()),
    # retrieve a course data
    path('detail-course/<int:pk>', DetailView.as_view()),
    # update course
    path('update-course/<int:pk>/', UpdateView.as_view()),
    # delete course
    path('update-course/<int:pk>/delete/', DeleteCourse.as_view()),
]