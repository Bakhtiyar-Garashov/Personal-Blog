from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
# Create your views here.


@api_view(['GET'])
def home(request):
    api_data = {'name': 'blog api', 'version': '1.0.0'}
    return Response(api_data)


@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    serialized_posts = PostSerializer(posts, many=True)
    return Response(serialized_posts.data)


@api_view(['POST'])
def create_post(request):
    serialized_post = PostSerializer(data=request.data)
    if serialized_post.is_valid():
        serialized_post.save()
    return Response(serialized_post.data)
