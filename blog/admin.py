from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Activity, User, Blog

# Register your models here.
admin.site.register(Post)
admin.site.register(Activity)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Blog)


