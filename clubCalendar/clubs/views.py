from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
import json
import datetime

from .models import *


def loginClub(request):
    return render(request, "LoginClub.html")

def loginUser(request):
    return render(request, "LoginUser.html")
def clubPage(request):
    return render(request, "ClubPage.html")

def signClub(request):
    return render(request, "SignClub.html")

def signUser(request):
    return render(request, "SignUser.html")
