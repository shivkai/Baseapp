from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
