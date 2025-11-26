from django.shortcuts import render, get_object_or_404
from home.models import category

# Create your views here.
def tag_detail(request, slug):
    print(slug)

    tag = get_object_or_404(category, slug=slug)
    print(tag)
    foods =tag.food_set.all()
    print(foods)
    all_tags = category.objects.all() 
    return render(request,'tag_detail.html',{"foods":foods,"tag":tag,"all_tags":all_tags})