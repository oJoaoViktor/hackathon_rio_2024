from django.urls import path
from read_ata import views

urlpatterns = [
    path('atendentes/', views.upload_pdf, name='upload_pdf'),
]
