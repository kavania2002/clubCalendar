from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import auth
import json
import datetime

from .models import *


def loginClub(request):
    clubs = Club.objects.all()
    posts = Post.objects.all()
    if request.method == "POST":
        name = request.POST['clubname']
        password = request.POST['password']
        club = Club.objects.filter(name = name)
        if (club.exists()):
            for i in club:
                if (i.password == password):
                    print("Successfully Logged In")
                    i.logged = True
                    i.save()
                    return redirect("userInterface")
            else:
                print("Unable to Login")
                messages.info(request,"Incorrect Password")
                return redirect("loginClub")
        else:
            messages.info(request,"Incorrect Name")
            print("Unable to Login")
            return redirect("loginClub")

    else:
        return render(request, "LoginClub.html")

def loginUser(request):
    clubs = Club.objects.all()
    posts = Post.objects.all()
    if (request.method == "POST"):
        email = request.POST['email']
        pwd = request.POST['password']
        pwd1 = request.POST['pwd2']

        users = User.objects.filter(email = email)
        if (pwd == pwd1):
            if (users.exists()):
                for i in users:
                    if (i.password == pwd):
                        i.logged = True
                        i.save()
                        print("Successfully Logged in")
                        return redirect("userInterface")

                else:
                    messages.info(request,"Incorrect Password")
                    print("Unable to Login")        
                    return redirect("loginUser")
            else:
                messages.info(request,"Incorrect Email")
                print("Invalid Username")
                return redirect("loginUser")
        else:
            messages.info(request,"Password not Matching")
            print("Password not matching")
            return render(request, "LoginUser.html")

    else: 
        return render(request, "LoginUser.html")

def clubPage(request, name):
    if (request.method == "POST"):
        pass
    else:
        if (User.objects.filter(logged = True).exists()):
            user = User.objects.get(logged = True)
        else:
            user = User.objects.filter(logged = True)
        club = Club.objects.get(name = name)
        posts = []
        for i in Post.objects.all():
            if i.clubName.name == name:
                posts.append(i)
        return render(request, "ClubPage.html", {'club':club, 'posts':posts,'user':user})
        

def signClub(request):
    clubs = Club.objects.all()
    posts = Post.objects.all()
    if (request.method == "POST"):
        name = request.POST['name']
        email = request.POST['email']
        pwd1 = request.POST['password']
        pwd2 = request.POST['pwd2']

        if (pwd1 == pwd2):
            if (Club.objects.filter(name = name).exists()):
                messages.info(request,"The club name already exists! Choose a different name")
                print("Club name is repated! Kindly pick a different name")
                return redirect("signClub")
            elif (Club.objects.filter(email = email).exists()):
                messages.info(request,"Email-ID is already being use! Try Login instead")
                print("This email-id is being used! Try login instead")
                return redirect("signClub")
            else:
                club = Club.objects.create(name = name, email = email, password = pwd1, logged = True)
                club.save()
                return redirect("userInterface")
        else:
            messages.info(request,"Password not matching")
            print("Password doesn't match")
            return redirect("signClub")
    else:
        return render(request, "SignClub.html")

def signUser(request):
    posts = Post.objects.all()
    clubs = Club.objects.all()
    if (request.method == "POST"):
        name = request.POST['fname']
        email = request.POST['email']
        phoneNo = request.POST['phoneNumber']
        pwd = request.POST['password']

        if (User.objects.filter(email = email).exists()):
            messages.info(request,"Email already exists")
            print("Email already exists")
            return redirect("signUser")
        else:
            user = User.objects.create( email = email, password = pwd, phoneNumber = phoneNo, name = name, logged = True)
            user.save()
            return redirect("userInterface")
    else:
        return render(request, "SignUser.html")
        
def singlePost(request,title):
    posts = Post.objects.all()
    clubs = Club.objects.all()
    if (request.method == "POST"):
        pass
    else:
        post = Post.objects.get(title = title)
        userLog = User.objects.filter(logged = True)
        clubLog = Club.objects.filter(logged = True)
        if (len(userLog) > 0):
            return render(request,"single.html", {'posts':posts, 'clubs':clubs, 'club':clubLog, 'user':userLog[0], 'post':post})
        elif (len(clubLog) > 0):
            return render(request,"single.html", {'posts':posts, 'clubs':clubs, 'club':clubLog[0], 'user':userLog, 'post':post})
        else:
            return render(request,"single.html", {'posts':posts, 'clubs':clubs, 'club':clubLog, 'user':userLog, 'post':post})



def userInterface(request):
    posts = Post.objects.all()
    clubs = Club.objects.all()
    if (request.method == "POST"):
        pass
    else:
        userLog = User.objects.filter(logged = True)
        clubLog = Club.objects.filter(logged = True)
        if (len(userLog) > 0):
            return render(request,"UserInterface.html", {'posts':posts, 'clubs':clubs, 'club':clubLog, 'user':userLog[0]})
        elif (len(clubLog) > 0):
            return render(request,"UserInterface.html", {'posts':posts, 'clubs':clubs, 'club':clubLog[0], 'user':userLog})
        else:
            return render(request,"UserInterface.html", {'posts':posts, 'clubs':clubs, 'club':clubLog, 'user':userLog})


def logout(request):
    club = Club.objects.filter(logged = True)
    user = User.objects.filter(logged = True)
    for i in club:
        i.logged = False
        i.save()

    for i in user:
        i.logged = False
        i.save()

    return redirect("userInterface")


def eventForm(request):
    posts = Post.objects.all()
    clubs = Club.objects.all()
    if (request.method == "POST"):
        clubLog = Club.objects.filter(logged = True)
        title = request.POST['name']
        link = request.POST['link']
        shortDesc = request.POST['shortDescri']
        longDesc = request.POST['message']
        meetLink = request.POST['meetLink']
        image = request.POST['imageUrl']
    
        post = Post.objects.create(clubName =  clubLog[0],title = title, link = link, sortDesc = shortDesc, description = longDesc, image = image, likes = 0)
        post.save()

        return redirect("userInterface")
    else:
        userLog = User.objects.filter(logged = True)
        clubLog = Club.objects.filter(logged = True)
        if (len(userLog) > 0):
            return render(request,"clubEventform.html", {'posts':posts, 'clubs':clubs, 'club':clubLog, 'user':userLog[0]})
        elif (len(clubLog) > 0):
            return render(request,"clubEventform.html", {'posts':posts, 'clubs':clubs, 'club':clubLog[0], 'user':userLog})
        else:
            return render(request,"clubEventform.html", {'posts':posts, 'clubs':clubs, 'club':clubLog, 'user':userLog})
