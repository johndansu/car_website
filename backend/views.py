from django.shortcuts import render
from django.http import HttpResponse

from backend.form import *

from django.contrib import messages
# Create your views here.

def login(request):
    return HttpResponse('<h1>Login Page</h1>')

def register(request):
    if request.method == 'POST':
        register = Register(request.POST)
        if register.is_valid():
            register.save()
            messages.success(request, 'User have been register')
    else:
        register = Register()            
    return render(request, 'frontend/register.html', { 'reg':register })


def dashboard(request):
    return render(request, 'backend/index.html')

    
def category_form(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            messages.success(request, 'Category Created')
    else:
        cat_form = CategoryForm()
    return render(request, 'backend/add-category.html', {'cat':cat_form})
    


    
