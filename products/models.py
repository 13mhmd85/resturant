from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from home.models import category

# Create your models here.
class Food(models.Model):
    
    productid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tag = models.ManyToManyField(category, blank=True)
    price = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to='image/',blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True,blank=True,null=True)
    description = models.TextField(default='default description')
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return f"{self.productid} - {self.name} - {self.slug}"
    
    class Meta:
        ordering = ['-updated']
        verbose_name='Food'
        
    def get_absolute_url(self):
        return reverse('home:detail',args=[self.slug])
    
    
class comment(models.Model):
    Food = models.ForeignKey(Food, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
    
    
    
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    situation = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user} - {self.Food.name} - {self.text[:40]}"

    
