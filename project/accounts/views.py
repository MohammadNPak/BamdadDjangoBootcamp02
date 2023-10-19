from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import reverse, redirect

# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, "accounts/login.html", {})
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect(reverse("index"))

        return render(request, "accounts/login.html", {})


def logout(request):
    if request.method == "GET":
        return render(request, "accounts/login.html", {})
    else:
        return render(request, "accounts/login.html", {})


def register(request):
    if request.method == "GET":
        return render(request, "accounts/register.html", {})
    else:
        return render(request, "accounts/register.html", {})
