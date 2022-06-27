from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
