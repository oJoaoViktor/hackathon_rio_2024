
from django.urls import path
from .views import *

urlpatterns = [
    path('', transpose_audio_for_text, name="audio_for_text")
]
