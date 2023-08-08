from django.contrib import admin
from .models import Poll, PollOption, Profile, Comment, Story, Base, Job

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'created',
        'about',
        'karma',
        'submitted_count',
    ]

    def submitted_count(self, obj):
        return obj.submitted.count()
    
    submitted_count.short_description = 'Submitted Count'

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'by',
        'type',
        'time',
        'kids_count',
    ]

    def kids_count(self, obj):
        return obj.kids.count()
    
    kids_count.short_description = 'Kids Count'

admin.site.register(Job)

admin.site.register(Story)

admin.site.register(Poll)

admin.site.register(PollOption)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'parent_id',
        'text',
    ]

    def parent_id(self, obj):
        return obj.parent.id if obj.parent else None
    
    parent_id.short_description = 'Parent ID'

    class Meta:
        # Add a related_name to avoid reverse query name clash
        unique_together = ('parent', 'base_ptr')
        related_name = 'comment_relations'

# Register your models here.
