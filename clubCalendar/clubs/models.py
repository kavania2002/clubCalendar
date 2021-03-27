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
    image = models.CharField(max_length=5000)
    logged = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    clubName = models.OneToOneField(Club, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100)
    likes = models.IntegerField()
