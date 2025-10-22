from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    
class Footer(models.Model):
    email = models.EmailField()
    address = models.TextField()
    def __str__(self):
        return self.email