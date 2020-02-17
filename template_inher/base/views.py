from django.shortcuts import render
from base.forms import *


def login(request):
    form = LoginForm()
    if request == "GET":
        form = form.LoginForm(request.GET)
    return render(request, "base/login.html", {"form": form})

def register(request):
    form = RegisterForm()
    if request == "GET":
        form = form.RegisterForm(request.GET)
    return render(request, "base/register.html", {"form": form})
