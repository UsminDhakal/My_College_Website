from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('',views.index, name="home"),
    path('programs',views.programs, name="program"),
  
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('online',views.online, name="online"),
    path('gallery',views.gallery, name="gallery")
    
]