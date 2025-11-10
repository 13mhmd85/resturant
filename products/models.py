from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Food(models.Model):
    
    productid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to='image/',blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True,blank=True,null=True)
    description = models.TextField(default='default description')
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return f"{self.productid} - {self.name} - {self.slug}"
    
    class Meta:
        ordering = ['-created']
        verbose_name='Food'
        
    def get_absolute_url(self):
        return reverse('home:detail',args=[self.slug])

    
