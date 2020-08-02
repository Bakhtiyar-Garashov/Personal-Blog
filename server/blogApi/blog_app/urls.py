from django.contrib import admin
from django.urls import path
from .views import (
    home,
    get_all_posts,
    create_post,
    post_detail)

urlpatterns = [
    path('v1/', home, name='home'),
    path('v1/posts', get_all_posts, name='posts'),
    path('v1/posts/create', create_post, name='create post'),
    path('v1/posts/<int:id>', post_detail, name='post detail'),
]
