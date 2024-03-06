from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=10, unique=True)
    # Do we need a model for a profile?

class Post(models.Model):
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Activity(models.Model):
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="activity"
    )
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type = models.IntegerField()


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comments"
    )
    approved = models.BooleanField(default=False)
