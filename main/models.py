from django.db import models
from django.contrib.auth.models import User

# TYPE=(("Job", "job"),
#     ("Story", "story"),
#     ("Comment", "comment"),
#     ("Poll", "poll"),
#     ("Pollopt", "pollopt"))


class Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    about = models.TextField(blank=True)
    karma = models.IntegerField(blank=True, default=1)
    # submitted = models.ManyToManyField('Base', related_name='submissions', blank=True)

    def __str__(self):
        return self.id.username


# class Base(models.Model):
#     id= models.AutoField(primary_key= True)
#     by= models.ForeignKey(User, on_delete= models.CASCADE)
#     type= models.CharField(choices=TYPE, max_length=10)
#     time= models.DateTimeField(auto_now_add= True)
#     kids= models.ManyToManyField('self', symmetrical= False, blank= True)

#     def __str__(self):
#         return f'{self.id}- {self.type} by {self.by}'
#     class Meta:
#         ordering= ["-time"]

# class Job(Base):
#     deleted= models.BooleanField(default= False)
#     title= models.CharField(max_length= 255, blank= True)

class Story(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    author = models.CharField(max_length=255, default="")
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=255, null=False, blank= True)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    comments = models.ManyToManyField('Comment', related_name='stories', blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "stories"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username}"

# class Comment(Base):
#     parent = models.ForeignKey(Base, on_delete=models.CASCADE, related_name= "base_comment")
#     text = models.TextField(blank= True)

# class Poll(Base):
#     descendants = models.IntegerField(blank= True)
#     score = models.IntegerField(blank= True)
#     title = models.CharField(max_length=255)
#     text = models.TextField(blank= True)

# class PollOption(Base):
#     parent = models.ForeignKey(Base, on_delete=models.CASCADE, related_name='options')
#     score = models.IntegerField(blank= True)


# class Comment(models.Model):


# Create your models here.
