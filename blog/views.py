from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, Event
from .forms import ProfileForm



# Create your views here.


# def view_profile(request):
#     profile = request.user.profile
#     return render(request, 'profile.html', {'profile': profile})

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'

class EventView(DetailView):
    model = Event
    template_name = 'event.html'





# def edit_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('view_profile')
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     return render(request, 'edit_profile.html', {'form': form})

# class PostList(generic.ListView):
#     model = Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        # Handle form submission
    #     return 
    # else:
    #     # Display empty form
        return render(request, 'create_post.html')


def register(request):
    if request.method == 'POST':
    #     # Handle registration form submission
    # else:
    #     # Display registration form
        return render(request, 'registration/register.html')

def index(request):
    return render(request, 'blog/index.html')

