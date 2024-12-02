from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.geos import Point
from .models import FloodZone, Tweet


class FloodZoneAdmin(LeafletGeoAdmin):
    list_display = ('title', 'posted_by','URL','image_URL', 'description', 'location','created_at')

admin.site.register(FloodZone,FloodZoneAdmin)



class TweetAdmin(LeafletGeoAdmin):
    list_display = ('tweet_id', 'username','text','geom', 'timestamp')

admin.site.register(Tweet,TweetAdmin)


import os
import pandas as pd
from django.conf import settings
from django.contrib.gis.geos import Point
from .models import Tweet


csv_file_path = os.path.join(settings.BASE_DIR, 'floodzoneapp', 'floodtweets.csv')


if not os.path.isfile(csv_file_path):
    raise FileNotFoundError(f"The file {csv_file_path} does not exist.")


flood_tweets = pd.read_csv(csv_file_path)


for index, row in flood_tweets.iterrows():
    tweet_id = row['tweet_id']
    username = row['username']
    text = row['text']
    latitude = row['latitude']
    longitude = row['longitude']


    point = Point(longitude, latitude)


    tweet, created = Tweet.objects.update_or_create(
        tweet_id=tweet_id,
        defaults={
            'username': username,
            'text': text,
            'geom': point
        }
    )

    if created:
        print(f"Created new tweet with tweet_id: {tweet_id}")
    else:
        print(f"Updated existing tweet with tweet_id: {tweet_id}")

