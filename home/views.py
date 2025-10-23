from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    products = models.Food.objects.all()
    footer = models.Footer.objects.all()
    print(products)
    return render(request,'home/index.html',context={'products':products,'footer':footer})