from django.db import models

# Create your models here.


class Post(models.Model):
    create_at = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()
