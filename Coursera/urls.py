from django.urls import path, include
from rest_framework import routers
from .views import detail, form, update, delete, coursesView, createView, detailView, updateView, deleteCourse, CourseApis,CourseNewApi, PaginationView, CourseView, TeacherView

router = routers.DefaultRouter()
# Define course api routers
router.register('api/courses', CourseApis, basename='Courses')
router.register('teacher', TeacherView, basename='teacher')

urlpatterns = [
    path('',include(router.urls)),
    # Paginating all courses data
    path('pagination/',PaginationView.as_view(), name='pagination'),
    # Listening, creating, updating and deleteing courses
    path('course-view/', CourseView.as_view(), name='course_view'),
    # retrieve course
    path('course-view/<int:id>', CourseView.as_view(), name='course_view'),
    # crud view for course instance
    path('course-new-api/', CourseNewApi.as_view(),name='course_new_api'),
    # retrieve course
    path('course-new-api/<int:id>', CourseNewApi.as_view(),name='course_new_api'),
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
    path('all-courses/', coursesView.as_view()),
    # create a new course
    path('create-course/', createView.as_view()),
    # retrieve a course data
    path('detail-course/<int:pk>', detailView.as_view()),
    # update course
    path('update-course/<int:pk>/', updateView.as_view()),
    # delete course
    path('update-course/<int:pk>/delete/', deleteCourse.as_view()),
]