from django.contrib import admin
from .models import Blog, Comment, Post

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass