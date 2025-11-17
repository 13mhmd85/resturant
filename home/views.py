from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import category
from products.models import *

from .models import Footer
# Create your views here.
def home(request):
    products = Food.objects.all()
    footer = Footer.objects.all()
    tag = category.objects.all()
    recent_product=Food.objects.order_by('-updated','-created')[:2]
    
    print(products)
    return render(request,'home/index.html',context={'products':products,'footer':footer,'recent':recent_product,'tag':tag})


def productdetail(request,slug):
    products = get_object_or_404(Food, slug=slug)
    
    
    return render(request, 'home/detail page/detail.html', context={'product':products})

def navbar_partial(request):
    context = {'name':'FoodLanD'}
    return render(request,'includes/navbar.html',context)