from django.contrib import admin
from .models import Blog, Comment, Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('content','author')
    search_fields = ['content']
    

    summernote_fields = ('content',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass