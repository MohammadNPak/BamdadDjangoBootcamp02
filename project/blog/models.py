from django.db import models

# Create your models here.


class Post(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.ImageField(upload_to="post/")

    def __str__(self):
        return f"post-{self.id}: {self.title}"


class Comment(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"comment-{self.id}: {self.body[:30]}"
