from django.contrib import admin
from .models import Poll, PollOption, Profile, Comment, Story, Base, Job

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'created',
        'about',
        'karma',
        'submitted'
    ]
    

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'by',
        'type',
        'time',
        'kids'
    ]
    

admin.site.register(Job)

admin.site.register(Story)

admin.site.register(Poll)

admin.site.register(PollOption)

admin.site.register(Comment)
# Register your models here.