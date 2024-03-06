from django.contrib import admin
from .models import Post, Comment, Activity, User

# Register your models here.
admin.site.register(Post)
admin.site.register(Activity)
admin.site.register(User)
admin.site.register(Comment)