from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
import json
import datetime

from .models import *


def loginClub(request):
    if request.method == "POST":
        name = request.POST['clubname']
        password = request.POST['password']
        club = Club.objects.filter(name = name)
        if (club.exists()):
            for i in club:
                if (i.password == password):
                    print("Successfully Logged In")
                    club.logged = True
                    return HttpResponse("Done")
            else:
                print("Unable to Login")
                return redirect("loginClub")
        else:
            print("Unable to Login")
            return redirect("loginClub")

    else:
        return render(request, "LoginClub.html")

def loginUser(request):
    return render(request, "LoginUser.html")

def clubPage(request):
    return render(request, "ClubPage.html")

def signClub(request):
    return render(request, "SignClub.html")

def signUser(request):
    return render(request, "SignUser.html")
