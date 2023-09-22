from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, "blog/about.html",{})

def blog(request):
    return render(request, "blog/blog.html",{})

def contact(request):
    return render(request, "blog/contact.html",{})

def features(request):
    return render(request, "blog/features.html",{})

def index(request):
    return render(request, "blog/index.html",{})


# about.html
# blog.html
# contact.html
# features.html
# index.html
