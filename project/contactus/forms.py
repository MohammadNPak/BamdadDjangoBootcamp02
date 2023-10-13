from django import forms
from .models import Ticket

# class TicketForm(forms.Form):
#     name = forms.CharField(max_length=150)
#     phone = forms.IntegerField()
#     email = forms.EmailField(max_length=200)
#     message = forms.CharField(widget=forms.Textarea)


class TicketForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Ticket
