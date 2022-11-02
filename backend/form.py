from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from frontend.models import *

class Register(UserCreationForm):
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password*', widget=forms.PasswordInput(
        attrs={'class':'form-control','maxlength':10, 'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Comfirm Password*' ,widget=forms.PasswordInput(
        attrs={'class':'form-control','maxlength':10, 'placeholder':'Re-Enter Password'}))

        
    class meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
    
    
    def save(self,commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save() 
            return user           