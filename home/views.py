from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout




def home(request):  
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return render(request,'home.html')