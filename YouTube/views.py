from django.shortcuts import render, get_object_or_404
from .models import Video
from django.db.models import Q
# Create your views here.
def list(request):
    # get requested data
    query = request.GET.get('q',None)
    # set all videos
    set = Video.objects.all()
    #? ¿valid data?
    if query is not None:
        # filter video
        set = set.filter(
            Q(title__icontains=query) | 
            Q(during__icontains=query) |
            Q(description__icontains=query) |
            Q(youtuber__icontains=query)
        )
    # build context
    context = {
        'Videos':set
    }
    return render(request,'main.html',context)

def video(request,id):
    # get instance/404 error
    instance = get_object_or_404(Video,id=id)
    # build context
    context = {
        'video': instance
    }
    return render(request, 'video.html',context)

def interface(request):
    return render(request,'Interface.html')