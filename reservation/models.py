from datetime import timezone

from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
# Create your models here.


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    tedad = models.IntegerField()
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.full_name} - {self.tedad} - {self.date} - {self.phone}"
