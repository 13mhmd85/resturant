from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import category
from products.models import *
from django.core.paginator import Paginator

from .models import Footer
# Create your views here.
def home(request):
    products = Food.objects.all()
    footer = Footer.objects.all()
    tag = category.objects.all()
    recent_product=Food.objects.order_by('-updated','-created')[:2]
    page_number = request.GET.get('page')
    paginator = Paginator(products, 6)
    page_obj = paginator.get_page(page_number)
    print(page_number)
    
    print(products)
    return render(request,'home/index.html',context={'page_obj':page_obj,'footer':footer,'recent':recent_product,'tag':tag})


def productdetail(request,slug):
    products = get_object_or_404(Food, slug=slug)
    if request.method == 'POST':
        user = request.user
        
        text = request.POST.get('text')
        comment.objects.create(user=user,text=text,Food=products)
    

    
    
    return render(request, 'home/detail page/detail.html', context={'product':products})

def navbar_partial(request):
    context = {'name':'FoodLanD'}
    return render(request,'includes/navbar.html',context)