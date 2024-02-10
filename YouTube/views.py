from django.shortcuts import render, get_object_or_404
from .models import Video
from django.db.models import Q

# Create your views here.
def list(request):
    query = request.GET.get('q',None)
    set = Video.objects.all()
    if query is not None:
        set = set.filter(
            Q(title__icontains=query) | 
            Q(during__icontains=query) |
            Q(description__icontains=query) |
            Q(youtuber__icontains=query)
        )
    context = {
        'Videos':set
    }
    return render(request,'main.html',context)

def video(request,id):
    instance = get_object_or_404(Video,id=id)
    context = {
        'video': instance
    }
    return render(request, 'video.html',context)

def interface(request):
    return render(request,'Interface.html')