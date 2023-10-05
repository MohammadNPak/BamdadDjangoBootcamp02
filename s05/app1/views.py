from django.shortcuts import render
from .models import User,Product
# Create your views here.


def user_list(request):

    return render(request,'app1/user-list.html',{"u":User.objects.all()})


def user_detail(request,id):
    
    return render(request,'app1/user-detail.html',{"u":User.objects.get(id=id)})