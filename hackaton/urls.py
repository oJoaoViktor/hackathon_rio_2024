
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('read_audio.urls')),
    path("", include("read_ata.urls")),
]
