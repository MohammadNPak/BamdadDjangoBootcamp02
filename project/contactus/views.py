import re

from django.shortcuts import render
from .models import Ticket
from django.contrib import messages
from django.shortcuts import redirect, reverse
from .forms import TicketForm


# Create your views here.


# def contact(request):
#     if request.method == "GET":
#         return render(request, "contactus/contact.html", {})
#     elif request.method == "POST":
#         name = request.POST["name"]
#         phone = request.POST["phone"]
#         email = request.POST["email"]

#         if re.match(r"[\w.-]{4,}@[\w.-]{3,}\.[\w.-]{3,}", email) is not None:
#             message = request.POST["message"]
#             ticket = Ticket.objects.create(
#                 name=name, phone=phone, email=email, message=message
#             )
#             ticket.save()
#             messages.add_message(
#                 request, messages.SUCCESS, f"your ticket was saved successfully!"
#             )
#         else:
#             messages.add_message(
#                 request, messages.ERROR, f"invalid email! ticket was not saved!!!"
#             )

#         return redirect(reverse("contact"))


def contact(request):
    if request.method == "GET":
        form = TicketForm()
        return render(request, "contactus/contact.html", {"form": form})

    elif request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            # ticket.save()
            # print(form.cleaned_data)
            # ticket = Ticket.objects.create(**form.cleaned_data)
            # ticket.save()
            form.save()
            messages.add_message(
                request, messages.SUCCESS, f"your ticket was saved successfully!"
            )
        else:
            messages.add_message(
                request, messages.ERROR, f"invalid email! ticket was not saved!!!"
            )

        return redirect(reverse("contact"))
