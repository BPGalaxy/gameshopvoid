from urllib import request

from django.shortcuts import render, redirect
from django.contrib import messages as ms
from django.contrib.auth.models import User
from home.models import Status
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
import random

def user_register(request):
    def generate_id():
        chars = [1,2,3,4,5,6,7,8,9,0,"q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
        unique_ID = ""
        for i in range(15):
            choice = random.choice(chars)
            unique_ID = unique_ID + str(choice)
        return unique_ID

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        users = User.objects.all()
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            for user in users:
                if str(cd['Username']) == str(user):
                    ms.error(request, "Username already exists")
                    return redirect("register")
                elif str(cd['Email']) == str(user.email):
                    ms.error(request, "Email already registered")
                    return redirect("register")
            User.objects.create_user(
                username=cd['Username'],
                email=cd['Email'],
                password=cd['Password'],
                first_name=cd['First_name'],
                last_name=cd['Last_name']
            )
            authenticated_user = authenticate(request, username=form.cleaned_data['Username'], password=form.cleaned_data['Password'])
            login(request, authenticated_user)
            Status.objects.create(username=authenticated_user, purchaseId=f"{generate_id()}")
            ms.success(request, "Account created successfully")
            return redirect("homepage")

    else:
        form = UserRegisterForm()
    return render(request, "forms/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            authenticated_user = authenticate(request, username=form.cleaned_data['Username'], password=form.cleaned_data['Password'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                ms.success(request, "Logged in successfully")
                return redirect("homepage")
            else:
                ms.error(request, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, "forms/login.html", {"form": form})

def user_logout(request):
    logout(request)
    ms.success(request, "Successfully logged out")
    return redirect("homepage")

