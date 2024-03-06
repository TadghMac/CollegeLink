from . import views
from django.urls import path


urlpatterns = [
    path('', views.Feed.as_view(), name='home'),
]