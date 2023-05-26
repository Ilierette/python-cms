from django.db import models
from django.utils.html import format_html

class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField("date published", null=True)
    event_date = models.DateTimeField("event date", null=True)
    description = models.TextField(max_length=1000, null=True)
    url = models.URLField(null=True)
    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"
    

class SocialMediaLink(models.Model):
    url = models.URLField(null=True)
    name = models.CharField(max_length=200, null=True)
    class Meta:
        verbose_name_plural = "Social Media"

class WishlistItem(models.Model):
    url = models.URLField(null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1000, null=True)
    class Meta:
        verbose_name_plural = "Wishlist"