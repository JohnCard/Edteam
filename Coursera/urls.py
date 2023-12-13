from django.urls import path
from .views import list,detail,form,update,delete,coursesView,createView,detailView,updateView,deleteCourse,CourseAPIView

urlpatterns = [
    path('courseApi/<int:id>',CourseAPIView.as_view()),
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