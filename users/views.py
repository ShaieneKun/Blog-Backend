from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import LoginForm
#from django.auth.
# Create your views here.


# Using generic view, CreateView. The fields var, sets which attributes of User will be required 
# This functionality is made using django's default create functionality
class CreateUser(CreateView):
    template_name = 'users/create.html'
    model = User
    fields = ['username', 'email', 'password']
