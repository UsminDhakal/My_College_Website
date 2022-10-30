from django.shortcuts import HttpResponse, render
from datetime import datetime
from app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def bsccsit(request):
    return render(request,"BSc.CSIT.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name, email=email,phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent..')
    
    return render(request,"contact.html")
    
    
def online(request):
    return render(request,"online.html")

def gallery(request):
    return render(request,"gallery.html") 

def programs(request):
    return render(request,"programs.html")

def bim(request):
    return render(request,"bim.html")

def mbs(request):
    return render(request,"mbs.html")

def bhm(request):
    return render(request,"bhm.html")

def bca(request):
    return render(request,"bca.html")

def bbs(request):
    return render(request,"bbs.html")