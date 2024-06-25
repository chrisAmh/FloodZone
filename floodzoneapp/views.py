from django.shortcuts import render,redirect
from .forms import FloodZoneForm
from .models import FloodZone
from .models import Tweet
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpRequest,HttpResponse
from datetime import datetime
from django.shortcuts import render
 

def home_view(request):
    posts = FloodZone.objects.all()
    return render(request,'floodzoneapp/home.html',{'posts': posts})


def floodzone_create(request):
    form = FloodZoneForm()       
    if request.method =='POST':
        form = FloodZoneForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    return render(request, 'floodzoneapp/post_create.html', {'form': form})

def floodzone_map(request):   
    return render(request, 'floodzoneapp/map.html')

def tweet_view(request):
    tweet_serialize = serialize('geojson',Tweet.objects.all())
    return HttpResponse(tweet_serialize,content_type='application/json')

