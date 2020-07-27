from django.contrib import admin
from django.urls import path
from .views import (
    home,
    get_all_posts,
    create_post)

urlpatterns = [
    path('v1/', home, name='home'),
    path('v1/posts', get_all_posts, name='posts'),
    path('v1/posts/create', create_post, name='create post'),
]
