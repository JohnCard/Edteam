from django.contrib import admin
from .models import Video, Youtuber, Anime

# Register your models here.
admin.site.register(Video)
admin.site.register(Anime)
admin.site.register(Youtuber)

