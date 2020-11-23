from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural='Category'

class Car(models.Model):
    car_type = models.CharField(max_length=60)

    def __str__(self):
        return self.car_type

class Plan(models.Model):
    plan_name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.plan_name

class User_plan(models.Model):
    user_plan_name =  models.ForeignKey(Plan,on_delete=models.CASCADE,blank=True,null=True)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True) 

    def __str__(self):
        return f'{self.user_name} is on a {self.user_plan_name} Plan'      

class Seller_Product(models.Model):
    car_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    car_name = models.CharField(max_length=80)
    car_model = models.CharField(max_length=80)
    car_year = models.CharField(max_length=80)
    car_type = models.ForeignKey(Car,on_delete=models.CASCADE)
    car_speed = models.DecimalField(max_digits=7,decimal_places=2)
    car_owner_location = models.CharField(max_length=80)
    car_image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    car_price = models.DecimalField(max_digits=12,decimal_places=2)
    car_description = models.TextField(default='',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_model

    @property
    def img_url(self):
        if self.car_image:
            return self.car_image.url
