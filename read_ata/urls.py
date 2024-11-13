from django.urls import path
from read_ata import views

urlpatterns = [
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
]
