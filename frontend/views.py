from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def error(request):
    return render(request, 'frontend/404error.html')

def about(request):
    return render(request, 'frontend/about-us.html')

def car(request):
    return render(request, 'frontend/car-detail.html')
