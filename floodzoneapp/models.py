from django.db import models
from django.contrib.gis.db import models as gis_models

class FloodZone(models.Model):
    title = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=500,null=True)
    URL = models.URLField(max_length=500,null=True)
    image_URL = models.URLField()
    description = models.TextField(blank=True, null=True)
    location = gis_models.PointField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.created_at

class Meta:
    ordering = ['created_at']

class Tweet(models.Model):
    tweet_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    text = models.TextField()
    Longitude = models.FloatField(blank=True,null=True)
    Latitude = models.FloatField(blank=True,null=True)
    geom = gis_models.PointField(Longitude,Latitude)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}: {self.text[:50]}'