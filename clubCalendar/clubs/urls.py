from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path("loginClub", views.loginClub, name = "loginClub"),
    path("clubPage/<name>", views.clubPage, name = "clubPage"),
    path("signClub", views.signClub, name = "signClub"),
    path("loginUser", views.loginUser, name = "loginUser"),
    path("signUser", views.signUser, name = "signUser"),
    path("singlePost/<title>", views.singlePost, name = "singlePost"),
    path("", views.userInterface, name = "userInterface"),
    path("logout",views.logout, name = "logout"),
    path('eventForm', views.eventForm, name="eventForm")

]