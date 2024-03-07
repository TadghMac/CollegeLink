from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post


def index(request):
    return render(request, 'blog/index.html')
#  2db9d4353ee5785b7c141ee118718490d94ab1fb
