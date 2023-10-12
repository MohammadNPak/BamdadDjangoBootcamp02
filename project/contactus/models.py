from django.db import models

# Create your models here.


class Ticket(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    message = models.TextField()
