from platform import platform
from turtle import title
from unicodedata import name
from django.db import models

'''
    Relationshops method
    One to one -> use One to One
    Many to one -> Use foreign key
    Many to many -> use many to many
'''

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist") # can be in one platform
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    