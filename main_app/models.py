from django.db import models

# Create your models here.

# class About(models.Model):
#     about = models.TextField(max_length=250)

class Photo(models.Model):    
    img_name = models.CharField(max_length=300)    
    img_src = models.ImageField(upload_to='photos/')

class Video(models.Model):    
    video_name = models.CharField(max_length=300)    
    video_url = models.FileField(upload_to='videos/',blank=True,null=True)
