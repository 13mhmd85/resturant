from django.db import models


# Create your models here.

class category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True,blank=True,null=True)

    def __str__(self):
        return self.title
    
    

    def __str__(self):
        return self.title

    
    
class Footer(models.Model):
    email = models.EmailField()
    address = models.TextField()
    phone=models.CharField(max_length=11)
    whatsapp=models.CharField(max_length=100,default='default text')
    telegram=models.CharField(max_length=100,default='default text')
    instagram=models.CharField(max_length=100,default='default text')
    def __str__(self):
        return self.email