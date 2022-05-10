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

def login(request):
    return render(request, 'frontend/login.html')

def contact(request):
    return render(request, 'frontend/contact-us.html')

def dashboard(request):
    return render(request, 'frontend/dashboard.html')

def wishlist(request):
    return render(request, 'frontend/wishlist.html')

def cart(request):
    return render(request, 'frontend/shopping-cart.html')


