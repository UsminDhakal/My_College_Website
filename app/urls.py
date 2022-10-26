from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('',views.index, name="home"),
    path('bim',views.bim, name="bim"),
    path('bsccsit',views.bsccsit, name="bsccsit"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('online',views.online, name="online"),
    path('gallery',views.gallery, name="gallery")
    
]