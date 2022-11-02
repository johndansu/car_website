from multiprocessing import context
from django.shortcuts import render
from frontend.models import Seller_Product,Plan,User_plan,Category
from django.core.exceptions import ObjectDoesNotExist

#for sendingmail import
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(name+' '+email+' '+phone)
        subject = 'Contact Us Form'
        context = {'name':name, 'email':email, 'phone':phone}
        html_message = render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'info@shocommsolutions.com'
        email_var = mail.send_mail(subject, plain_message, from_email,['dansu.jw@gmail.com',], html_message=html_message, fail_silently=True)
        if email_var:
            messages.success(request, 'Email sent successfully')
        else:
            messages.error(request, 'Email not sent')   
    return render(request, 'frontend/contact-us.html')

def blog(request):
    return render(request, 'frontend/blog.html')

def login(request):
    return render(request, 'frontend/login.html')

def cart(request):
    return render(request, 'frontend/shopping-cart.html')
