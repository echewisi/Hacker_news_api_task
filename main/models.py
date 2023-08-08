from django.db import models
from django.contrib.auth.models import User

TYPE=(("Job", "job"),
    ("Story", "story"),
    ("Comment", "comment"),
    ("Poll", "poll"),
    ("Pollopt", "pollopt"))



class Profile(models.Model):
    id= models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    created= models.DateTimeField(auto_now_add= True)
    about= models.TextField(blank= True)
    karma= models.IntegerField(blank= True, default=1)
    submitted = models.ManyToManyField('Base', related_name='submissions', blank=True)
    
    def __str__(self):
        return self.id
    

class Base(models.Model):
    id= models.AutoField(primary_key= True)
    by= models.ForeignKey(User, on_delete= models.CASCADE)
    type= models.CharField(choices=TYPE, max_length=10)
    time= models.DateTimeField(auto_now_add= True)
    kids= models.ManyToManyField('self', symmetrical= False, blank= True)
    
    def __str__(self):
        return f'{self.id}- {self.type} by {self.by}'  
    class Meta:
        ordering= ["-time"]
        
class Job(Base):
    deleted= models.BooleanField(default= False)
    title= models.CharField(max_length= 255)

class Story(Base):
    descendants= models.IntegerField()
    score= models.IntegerField(default= 0)
    title= models.CharField(max_length=255)
    url= models.URLField()

class Comment(Base):
    parent = models.ForeignKey(Base, on_delete=models.CASCADE)
    text = models.TextField()
    
class Poll(Base):
    descendants = models.IntegerField()
    score = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    
class PollOption(Base):
    parent = models.ForeignKey(Base, on_delete=models.CASCADE, related_name='options')
    score = models.IntegerField()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        type= self.type
        if type== "Job":
            Job.objects.create(type= self)
        elif type== "Story":
            Story.objects.create(type= self)
        elif type== "Comment":
            Comment.objects.create(type= self)
        elif type== "Poll":
            Poll.objects.create(type= self)
        elif type== "Pollopt":
            PollOption.objects.create(type=self)
    
    
# class Comment(models.Model):
    
    
    

# Create your models here.
