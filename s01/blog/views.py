from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'blog/index.html', context={"name": "mohammad"})


def profile(request):
    return render(request, "blog/user_profile.html", {"username": "mohammad"})
