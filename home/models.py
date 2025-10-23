from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to='image/')
    description = models.TextField(default='default description')
    def __str__(self):
        return self.name
    
class Footer(models.Model):
    email = models.EmailField()
    address = models.TextField()
    phone=models.CharField(max_length=11)
    whatsapp=models.CharField(max_length=100,default='default text')
    telegram=models.CharField(max_length=100,default='default text')
    instagram=models.CharField(max_length=100,default='default text')
    def __str__(self):
        return self.email