from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from . import models


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        print(username, password, email, fullname)
        if username and password and email and fullname:
            user = models.User.objects.create(username=username, password=password, email=email, name=fullname)
            return redirect('/')

    return render(request, 'account/register.html')
def login_view(request):
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
