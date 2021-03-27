from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200) 
    email = models.EmailField(max_length=100)
    phoneNumber = models.IntegerField(null=True)

class Club(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    image = models.ImageField()
    logged = models.BooleanField(default=False)