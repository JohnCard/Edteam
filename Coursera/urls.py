from django.urls import path,include
from rest_framework import routers
from .views import detail,form,update,delete,coursesView,createView,detailView,updateView,deleteCourse,CourseApis,NewApi,PaginationView, PaginationViewVehicle, Methods, CourseView, TeacherView

router = routers.DefaultRouter()
router.register('api/courses', CourseApis,basename='Courses')
router.register('teacher', TeacherView, basename='teacher')

urlpatterns = [
    path('',include(router.urls)),
    path('Pagination/',PaginationView.as_view(),name='pagination'),
    path('PaginationV/',PaginationViewVehicle.as_view(),name='pagination-vehicle'),
    path('courseview/', CourseView.as_view(), name='courseview'),
    path('courseview/<int:id>', CourseView.as_view(), name='courseview'),
    path('Methods/',Methods.as_view(),name='methods'),
    path('NewApi/',NewApi.as_view(),name='new-api'),
    path('NewApi/<int:id>',NewApi.as_view(),name='new-api'),
    # path('Courses/',list),
    path('Detail/<int:id_course>',detail),
    path('Form/',form),
    path('Update/<int:id_course>',update),
    path('Delete/<int:id_course>', delete),
    path('allCourses/',coursesView.as_view()),
    path('createCourse/',createView.as_view()),
    path('detailCourse/<int:pk>',detailView.as_view()),
    path('updateCourse/<int:pk>/',updateView.as_view()),
    path('updateCourse/<int:pk>/delete/',deleteCourse.as_view()),
]