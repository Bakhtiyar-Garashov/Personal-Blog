from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    api_data = {'name': 'blog api', 'version': '1.0.0'}
    return Response(api_data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_all_posts(request):
    posts = Post.objects.all()
    serialized_posts = PostSerializer(posts, many=True)
    return Response(serialized_posts.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_post(request):
    serialized_post = PostSerializer(data=request.data)
    if serialized_post.is_valid():
        serialized_post.save()

    return Response({"success": "New data added successfully"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def post_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    serialized_posts = PostSerializer(posts)
    return Response(serialized_posts.data, status=status.HTTP_200_OK)
