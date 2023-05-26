from rest_framework import serializers
from links.models import Event, SocialMediaLink, WishlistItem, AffiliateLink

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','name', 'pub_date', 'event_date', 'description', 'url']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = ['id', 'name', 'url']

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ['id', 'name', 'url', 'description']


class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateLink
        fields = ['id', 'name', 'url', 'description']