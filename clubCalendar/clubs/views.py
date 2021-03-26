from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
import json
import datetime

from .models import *

def loginUser(request):
    if request.method == "POST":
        
    else:
        return render(request, "LoginUser.html")