import tweepy
import os
from datetime import datetime
import django
from django.conf import settings
from django.contrib.gis.geos import Point

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FloodZone.settings')
django.setup()

from floodzoneapp.models import Tweet

# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Set up Tweepy authentication
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define the search query
search_query = 'flood -filter:retweets'
geocode = '5.6037,-0.1870,20km'  # Geocode for Accra with a 20km radius

# Retrieve geotagged tweets
tweets = api.search_tweets(q=search_query, geocode=geocode, count=100, tweet_mode='extended')

for tweet in tweets:
    if tweet.coordinates:
        longitude, latitude = tweet.coordinates['coordinates']
        text = tweet.full_text
        username = tweet.user.screen_name
        timestamp = tweet.created_at

        # Save tweet to the database
        location = Point(longitude, latitude)
        Tweet.objects.create(
            tweet_id=tweet.id_str,
            username=username,
            text=text,
            location=location,
            timestamp=timestamp
        )
        print(f'Tweet by {username} at {latitude},{longitude} saved.')
