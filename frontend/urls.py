from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.compare, name='compare'),
    path('foreign-page/', views.foreign, name='foreign'),
    path('nigerian-page/', views.nigerian, name='nigerian'),
    path('about-page/', views.about, name='about'),
    path('contact-page/', views.contact, name='contact'),

]