from django import forms
from .models import FloodZone
from leaflet.forms.widgets import LeafletWidget


class FloodZoneForm(forms.ModelForm):
    class Meta:
        model = FloodZone
        fields = ['title', 'posted_by','image_URL', 'description','location']
        widgets = {
            'location': LeafletWidget(),
            }
