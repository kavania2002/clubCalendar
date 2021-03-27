from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200) 
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phoneNumber = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "static/img")
    logged = models.BooleanField(default=False)

    def __str__(self):
        return self.name