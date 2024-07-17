from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializers
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'body', 'categories__category', 'author__username']

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers