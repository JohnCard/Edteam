from django.contrib import admin
from .models import Video, Youtuber

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')
    ordering = ['id', ]
    
class YoutuberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', )
    ordering = ['id', ]

admin.site.register(Video, VideoAdmin)
admin.site.register(Youtuber, YoutuberAdmin)

