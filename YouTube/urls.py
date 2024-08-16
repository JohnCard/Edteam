from django.urls import path
from .views import list,video, interface

urlpatterns = [
    # list videos
    path('videos/', list),
    # retrieve one video
    path('video/<int:id>', video),
    # user interface
    path('interface/', interface)
]