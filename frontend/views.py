from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def compare(request):
    return render(request, 'frontend/compare.html')

def foreign(request):
    return render(request, 'frontend/grid.html')

def nigerian(request):
    return render(request, 'frontend/list.html')

def about(request):
    return render(request, 'frontend/about-us.html')

def contact(request):
    return render(request, 'frontend/contact-us.html')

def blog(request):
    return render(request, 'frontend/blog.html')


