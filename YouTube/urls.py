from django.urls import path
from .views import list,video, interface

urlpatterns = [
    # list videos
    path('Videos/',list),
    # retrieve one video
    path('video/<int:id>',video),
    # user interface
    path('Interface/',interface)
]