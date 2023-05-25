from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField("date published", null=True)
    event_date = models.DateTimeField("event date", null=True)
    description = models.TextField(max_length=1000, null=True)
    url = models.URLField(null=True)
