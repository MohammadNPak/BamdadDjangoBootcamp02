from django.shortcuts import render
from .models import Ticket
from django.contrib import messages
from django.shortcuts import redirect, reverse

# Create your views here.


def contact(request):
    if request.method == "GET":
        return render(request, "contactus/contact.html", {})
    elif request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        message = request.POST["message"]

        ticket = Ticket.objects.create(
            name=name, phone=phone, email=email, message=message
        )
        ticket.save()
        messages.add_message(
            request, messages.SUCCESS, f"your ticket was saved successfully!"
        )

        return redirect(reverse("contact"))
