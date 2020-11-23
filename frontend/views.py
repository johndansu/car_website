from django.shortcuts import render
from frontend.models import Seller_Product,Plan,User_plan,Category
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def compare(request):
    return render(request, 'frontend/compare.html')

def foreign(request):
    return render(request, 'frontend/grid.html')

def nigerian(request):
    lst = Seller_Product.objects.all().filter(category=1)
    return render(request, 'frontend/list.html', {'lt':lst })

def about(request):
    return render(request, 'frontend/about-us.html')

def contact(request):
    return render(request, 'frontend/contact-us.html')

def blog(request):
    return render(request, 'frontend/blog.html')


