from django.contrib import admin
from .models import Profile
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'url'
    ]
    
    search_fields=[
        'title',
        'author'
    ]
    
admin.site.register(Profile)