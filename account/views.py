from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages

from . import models
from django.contrib.auth.models import User



# Create your views here.
def register(request):
    if request.user.is_authenticated:
        print("logged in")
        return redirect('/')
    # این وصله به مدلی که خودم ساختم (۱)

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     email = request.POST.get('email')
    #     fullname = request.POST.get('fullname')
    #     print(username, password, email, fullname)
    #     if username and password and email and fullname:
    #         user = models.User.objects.create(username=username, password=password, email=email, name=fullname)
    #         return redirect('/')

    # این وصله به مدل پیشفرض جنگو (۲)
    context = {'error':[]}
    errors = False
    if request.method == 'POST':
        first_name =request.POST.get('first_name')
        email =request.POST.get('email')
        username =request.POST.get('username')
        password1 =request.POST.get('password1')
        password2 =request.POST.get('password2')
        if password1 != password2:
            context["error"].append('Passwords do not match')
            errors = True
        if User.objects.filter(username=username):
            context["error"].append('Username already exists')
            errors = True
        if User.objects.filter(email=email):
            context["error"].append('Email already exists')
            errors = True
        if errors == True:
            return render(request, 'account/register.html', context)
        
        user = User.objects.create_user(first_name=first_name,username=username, email=email, password=password1)
        
        login(request, user)
        return redirect('/')

    return render(request, 'account/register.html')

def edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            user.first_name = request.POST.get('first_name')or ''
            user.last_name = request.POST.get('last_name')or ''
            user.email = request.POST.get('email')
            user.save()
            return redirect('account:user_page') 

        return render(request, 'account/edit_profile.html')
    else:
        return redirect('account:login')








def login_view(request):
    if request.user.is_authenticated:
        print("logged in")
        return redirect('/')
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user.first_name)
            print('succses login')
            login(request, user)
            return redirect('/')
        else:
            print('login failed')
            return render(request, 'account/login.html', {'error': 'نام کاربری یا رمز اشتباه است.'})
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def user_page(request):
    if request.user.is_authenticated:
        return render(request, 'account/userpage.html')
    else:
        return redirect('/login')
