from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path("loginClub", views.loginClub, name = "loginClub"),
    path("clubPage", views.clubPage, name = "clubPage"),
    path("signClub", views.signClub, name = "signClub"),
    path("loginUser", views.loginUser, name = "loginUser"),
    path("signUser", views.signUser, name = "signUser"),
    path("singlePost", views.singlePost, name = "singlePost"),
    path("UI", views.userInterface, name = "userInterface"),
    path("newPost", views.newPost, name = "newPost")

]