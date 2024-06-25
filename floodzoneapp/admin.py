from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import FloodZone, Tweet


class FloodZoneAdmin(LeafletGeoAdmin):
    list_display = ('title', 'posted_by','URL','image_URL', 'description', 'location','created_at')

admin.site.register(FloodZone,FloodZoneAdmin)



class TweetAdmin(LeafletGeoAdmin):
    list_display = ('tweet_id', 'username','text','geom', 'timestamp')

admin.site.register(Tweet,TweetAdmin)



