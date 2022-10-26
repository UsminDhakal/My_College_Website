from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return render(request,"index.html")

def bsccsit(request):
    return render(request,"BSc.CSIT.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
    
def online(request):
    return render(request,"online.html")

def gallery(request):
    return render(request,"gallery.html") 

def programs(request):
    return render(request,"programs.html")

def bim(request):
    return render(request,"bim.html")