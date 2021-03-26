from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path("loginClub", views.loginClub, name = "loginClub"),
    path("loginUser", views.loginUser, name = "loginUser")
]