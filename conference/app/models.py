# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Speaker(models.Model):
    speaker=models.OneToOneField(User, on_delete="CASCADED",related_name="speaker")
    picture = models.ImageField(upload_to='profile_pics',default='None.png')
    bio = models.TextField(max_length=1000,blank=True)
    twitter= models.CharField(max_length=16,blank=True)
    facebook= models.CharField(max_length=66,blank=True)
    def __str__(self):
    	return self.speaker.username
class session(models.Model):
    title=models.CharField(max_length=50)
    abstract=models.TextField(max_length=2000)
    speaker=models.ForeignKey(Speaker,on_delete='DO_NOTHING',related_name='session_speaker')
    created=models.DateTimeField(blank=True,null=True)#"creation_date"
    session_date=models.DateTimeField(blank=True,null=True)#"happening date!"
    venue=models.CharField(max_length=150,null=True)
    going=models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('app:session_detail',kwargs={'pk':self.pk})


class Visitor(models.Model):
    V_name=models.CharField(max_length=25,blank=True)
    V_email=models.CharField(max_length=40,blank=True)
    V_message=models.CharField(max_length=40,blank=True)
    def __str__(self):
        return self.V_name

class Vcount(models.Model):
    session=models.ForeignKey(session,on_delete='DO_NOTHING',related_name='session_title')
    visitor=models.ForeignKey(Visitor,on_delete='DO_NOTHING',related_name='visitor_name')
