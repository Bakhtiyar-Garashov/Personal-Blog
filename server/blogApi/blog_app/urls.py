from .views import (
    home,
    get_all_posts,
    create_post,
    post_detail)
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Blog project")


urlpatterns = [
    path('doc', schema_view, name="Api documentation"),
    path('', home, name='home'),
    path('posts', get_all_posts, name='posts'),
    path('posts/create', create_post, name='create post'),
    path('posts/<int:id>', post_detail, name='post detail'),
]
