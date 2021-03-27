from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import auth
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
    if (request.method == "POST"):
        email = request.POST['email']
        pwd = request.POST['password']
        pwd1 = request.POST['pwd2']

        user = User.objects.filter(email = email)
        if (pwd == pwd1):
            if (user.exists()):
                for i in user:
                    if (i.password == pwd):
                        print("Successfully Logged in")
                        return HttpResponse("Done USer")
                else:
                    print("Unable to Login")        
                    return redirect("loginUser")
            else:
                print("Invalid Username")
                return redirect("loginUser")
        else:
            print("Password not matching")
            return render(request, "LoginUser.html")

    else: 
        return render(request, "LoginUser.html")

def clubPage(request):
    return render(request, "ClubPage.html")

def signClub(request):
    if (request.method == "POST"):
        name = request.POST['name']
        email = request.POST['email']
        pwd1 = request.POST['password']
        pwd2 = request.POST['pwd2']

        if (pwd1 == pwd2):
            if (Club.objects.filter(name = name).exists()):
                print("Club name is repated! Kindly pick a different name")
                return redirect("signClub")
            elif (Club.objects.filter(email = email).exists()):
                print("This email-id is being used! Try login instead")
                return redirect("signClub")
            else:
                club = Club.objects.create(name = name, email = email, password = pwd1, logged = True)
                club.save()
                return HttpResponse("Club created")
        else:
            print("Password doesn't match")
            return redirect("signClub")
    else:
        return render(request, "SignClub.html")

def signUser(request):
    if (request.method == "POST"):
        name = request.POST['fname']
        email = request.POST['email']
        phoneNo = request.POST['phoneNumber']
        pwd = request.POST['password']

        if (User.objects.filter(email = email).exists()):
            print("Email already exists")
            return redirect("signUser")
        else:
            user = User.objects.create( email = email, password = pwd)
            user.name = name
            user.phoneNumber = phoneNo
            user.email = email
            user.save()
            return HttpResponse("User Created")
    else:
        return render(request, "SignUser.html")
