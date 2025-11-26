from django.shortcuts import render, redirect
from django_jalali.db import models as jmodels
from pyexpat.errors import messages
from persiantools.jdatetime import JalaliDate
from .models import Reservation
# Create your views here.
def reserv(request):
    if not request.user.is_authenticated:
        # messages.error(request, "قبل از رزرو باید وارد حساب شوید ⚠️")
        return redirect('account:login',context={'error':'قبل از اینکه شما بخواهید میز رزرو کنید میبایست به اکانت خود وارد شوید ⚠️'})
        
    if request.method == 'POST':

        username = request.user
        full_name = request.POST.get('full_name')
        phone_number = int(request.POST.get('phone_number'))
        email = request.POST.get('email')
        tedad = int(request.POST.get('tedad'))
        # دریافت تاریخ شمسی از input
        date_fa = request.POST.get('date_fa', '').strip()

        # تبدیل اعداد فارسی به انگلیسی
        persian_numbers = "۰۱۲۳۴۵۶۷۸۹"
        english_numbers = "0123456789"
        for p, e in zip(persian_numbers, english_numbers):
            date_fa = date_fa.replace(p, e)

        if date_fa:
            year, month, day = map(int, date_fa.split('/'))
            date_miladi = JalaliDate(year, month, day).to_gregorian()
        else:
            date_miladi = None  # یا تاریخ پیش‌فرض
        print(username)
        print(full_name)
        print(phone_number)
        print(email)
        print(tedad)
        print(date_fa)
        print(date_miladi)
        Reservation.objects.create(user=username,full_name=full_name,email=email,phone=phone_number,tedad=tedad,date=date_miladi)
        return redirect('home:home')
    return render(request,'reservation/reservation.html')