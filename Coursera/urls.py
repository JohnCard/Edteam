from django.urls import path,include
from rest_framework import routers
from .views import list,detail,form,update,delete,coursesView,createView,detailView,updateView,deleteCourse,CourseApi,CourseApis,NewApi,PaginationView

router = routers.DefaultRouter()
router.register('api/courses', CourseApis,basename='Courses')
urlpatterns = [
    path('',include(router.urls)),
    # path('courseApi/<int:id>',CourseApi.as_view(),name='course-api'),
    path('Pagination/',PaginationView.as_view(),name='pagination'),
    path('NewApi/',NewApi.as_view(),name='new-api'),
    path('courseApi/',CourseApi.as_view(),name='course-api'),
    path('Courses/',list),
    path('Detail/<int:id_course>',detail),
    path('Form/',form),
    path('Update/<int:id_course>',update),
    path('Delete/<int:id_course>', delete),
    path('allCourses/',coursesView.as_view()),
    path('createCourse/',createView.as_view()),
    path('detailCourse/<int:pk>',detailView.as_view()),
    path('updateCourse/<int:pk>/',updateView.as_view()),
    path('updateCourse/<int:pk>/delete/',deleteCourse.as_view())
]