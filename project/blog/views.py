from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.


def about(request):
    return render(request, "blog/about.html", {})


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def post_detail(request, id):
    post_object = Post.objects.get(id=id)
    if request.method == "GET":
        return render(request, "blog/post_detail.html", {"post_from_view": post_object})
    elif request.method == "POST":
        # print(request.POST["comment_body"])

        comment_body = request.POST["comment_body"]
        comment = Comment.objects.create(body=comment_body, post=post_object)
        comment.save()
        messages.add_message(request, messages.INFO, f"comment was saved successfully!")
        return redirect(reverse("post-detail", kwargs={"id": id}))


# http request method:          crud operation in database
# get                           retrive select
# post                          create insert
# put                           update
# delete                        delete


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
