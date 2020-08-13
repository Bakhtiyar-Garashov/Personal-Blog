from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

from .views import create_post, get_all_posts, home, post_detail, post_update, post_delete

schema_view = get_swagger_view(title="Blog project")


urlpatterns = [
    path('doc', schema_view, name="Api documentation"),
    path('', home, name='home'),
    path('posts', get_all_posts, name='posts'),
    path('posts/create', create_post, name='create post'),
    path('posts/<slug>', post_detail, name='post detail'),
    path('posts/<slug>/update', post_update, name='post update'),
    path('posts/<slug>/delete', post_delete, name='post delete'),
]
