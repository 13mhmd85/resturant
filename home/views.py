from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from products.models import *

from .models import Footer
# Create your views here.
def home(request):
    products = Food.objects.all()
    footer = Footer.objects.all()
    
    print(products)
    return render(request,'home/index.html',context={'products':products,'footer':footer,})


def productdetail(request,slug):
    products = get_object_or_404(Food, slug=slug)
    
    print(products.slug)
    return render(request, 'home/detail page/detail.html', context={'product':products})