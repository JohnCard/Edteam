from django.urls import path,include
from .views import list,video, interface

urlpatterns = [
    path('Videos/',list),
    path('video/<int:id>',video),
    path('Interface/',interface)
]