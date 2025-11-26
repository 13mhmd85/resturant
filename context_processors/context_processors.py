from home.models import *




def tags(request):
    tag = category.objects.all()
    return {'tag':tag}


