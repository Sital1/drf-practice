from turtle import update
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

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

class Reviews(models.Model):
       ## User foreign key
       review_user = models.ForeignKey(User, on_delete=models.CASCADE)
       ## with validators
       rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
       description = models.CharField(max_length=200, null=True)
       created = models.DateTimeField(auto_now_add=True)
       update = models.DateTimeField(auto_now=True)
       active = models.BooleanField(default=True)
       
       ## Connection between watchlist. One watchlist to many review
       watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
       
       def __str__(self):
           return str(self.rating) + " | " + self.watchlist.title 