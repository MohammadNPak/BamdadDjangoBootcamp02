from django.db import models

# Create your models here.


class User(models.Model):
    name = models.TextField()


class Product(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_product")