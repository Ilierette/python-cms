from rest_framework import serializers
from links.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'pub_date', 'event_date', 'description', 'url']