from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Activity, User, Blog

# Register your models here.


from .models import Blog, User, Post, Activity, Comment
# Register your models here
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

