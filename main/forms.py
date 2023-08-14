from django import forms
from .models import Profile
from .models import Story


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'karma']

class StoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'author', 'url', 'score']  # Add other fields as needed
