from django.urls import path
from frontend import views
app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('error/', views.error, name='error'),
    path('car/', views.car, name='car'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
]