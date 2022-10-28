from datetime import datetime
from email.policy import default
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()
    
class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date_released = models.DateField(default= datetime.today)
    likes = models.IntegerField()
    
class Lyric(models.Model):
    content = models.CharField(max_length=800)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
