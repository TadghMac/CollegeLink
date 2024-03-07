from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for your user profile if needed
    # Example:
    # bio = models.TextField()
# Modify the Post and Comment models to use the User model or UserProfile model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = SummernoteTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_on"]

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    approved = models.BooleanField(default=False)
    # Do we need a model for a profile?


class Activity(models.Model):
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="activity"
    )
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type = models.IntegerField()
    