from rest_framework import serializers
from main.models import Story
from main.models import User
from django.contrib.auth import authenticate

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Story
        fields= "__all__"