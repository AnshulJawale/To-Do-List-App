from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.
def register(request : HttpRequest):   
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save() 
            return redirect("/")
    else:
        register_form =  RegisterForm()
    return render(request, "register.html", {"form":register_form})