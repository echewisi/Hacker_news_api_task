from django.shortcuts import render
from rest_framework import generics
from main.models import Story
from .serializers import StorySerializer

class StoryList(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class StoryCreate(generics.CreateAPIView):
    serializer_class = StorySerializer


# Create your views here.
