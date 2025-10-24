from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.
def home(request):
    products = models.Food.objects.all()
    footer = models.Footer.objects.all()
    print(products)
    return render(request,'home/index.html',context={'products':products,'footer':footer})


def detail(request,id):
    products = get_object_or_404(models.Food, productid=id)
    print(products)


    return render(request,'detail page/detail.html',context={'product':products})