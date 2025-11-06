from django.db import models

# Create your models here.
class Food(models.Model):
    productid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to='image/')
    description = models.TextField(default='default description')
    def __str__(self):
        return f"{self.productid} - {self.name}"