from django.shortcuts import render, redirect
from django_jalali.db import models as jmodels
from pyexpat.errors import messages

from .models import Reservation
# Create your views here.
def reserv(request):
    if not request.user.is_authenticated:
        # messages.error(request, "قبل از رزرو باید وارد حساب شوید ⚠️")
        return redirect('account:login',context={'error':'قبل از اینکه شما بخواهید میز رزرو کنید میبایست به اکانت خود وارد شوید ⚠️'})
        
    if request.method == 'POST':

        username = request.user
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        tedad = request.POST.get('tedad')
        date = request.POST.get('date')
        print(username)
        print(full_name)
        print(phone_number)
        print(email)
        print(tedad)
        print(date)
        Reservation.objects.create(user=username,full_name=full_name,email=email,phone=phone_number,tedad=tedad)
        return redirect('home:home')
    return render(request,'reservation/reservation.html')