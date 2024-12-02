from django.core.management.base import BaseCommand
import os
import django
import tweepy
from floodzoneapp.models import Tweet
from django.contrib.gis.geos import Point

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FloodZone.settings')
django.setup()

class Command(BaseCommand):
    help = 'Fetch geotagged tweets about floods'

    def handle(self, *args, **kwargs):
        # Set up Django environment
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
                Tweet.objects.create(
                    tweet_id=tweet.id_str,
                    username=username,
                    text=text,
                    geom=Point(longitude, latitude),
                    timestamp=timestamp
                )
                print(f'Tweet by {username} at {latitude},{longitude} saved.')
                self.stdout.write("Fetching tweets completed.")
