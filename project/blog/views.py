from django.shortcuts import render
from .models import Post


# Create your views here.

def about(request):
    return render(request, "blog/about.html", {})


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def post_detail(request, id):
    # print(id)
    post_object = Post.objects.get(id=id)
    post_object.comment_set.all()
    return render(request, "blog/post_detail.html", {"post_from_view": post_object})


def contact(request):
    return render(request, "blog/contact.html", {})


def features(request):
    return render(request, "blog/features.html", {})


def index(request):
    return render(request, "blog/index.html", {})


# about.html
# blog.html
# contact.html
# features.html
# index.html
