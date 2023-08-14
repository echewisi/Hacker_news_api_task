from django.urls import path
from .views import StoryList, StoryCreate

urlpatterns = [
    path('api/items/', StoryList.as_view(), name='story-list'),
    path('api/items/create/', StoryCreate.as_view(), name='story-create'),
]
