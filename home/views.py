from django.shortcuts import render, get_object_or_404
from products.models import *
from .models import Footer
# Create your views here.
def home(request):
    products = Food.objects.all()
    footer = Footer.objects.all()
    print(products)
    return render(request,'home/index.html',context={'products':products,'footer':footer})


def productdetail(request,id):
    products = get_object_or_404(models.Food, productid=id)
    print(products)


    return render(request,'detail page/detail.html',context={'product':products})