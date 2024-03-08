
from . import views
from django.urls import path
from .views import ProfileView, EventView


urlpatterns = [
    # path('', views.PostList.as_view(), name='post_list'),
    # path('post/create/', views.create_post, name='create_post'),
    # path('profile/', views.view_profile, name='view_profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:pk', ProfileView.as_view(), name ='view_profile'),
     path('event/<int:pk', EventView.as_view(), name ='view_event'),
]


# urlpatterns = [
#     path('', views.index, name='index')
# 2db9d4353ee5785b7c141ee118718490d94ab1fb
# ]