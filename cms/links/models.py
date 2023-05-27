from django.db import models


class Event(models.Model):
    # bieżące wydarzenia widoczne na stronie głównej
    # widoczność regulowana przez datę publikacji

    name = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField("date published", null=True)
    event_date = models.DateTimeField("event date", null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    url = models.URLField(null=True)

    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"
        ordering = ["event_date"]

    def __str__ (self):
        return(self.name)
    

class SocialMediaLink(models.Model):
    # lista social mediów z ikonami np: w nagłówku

    url = models.URLField(null=True)
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __str__ (self):
        return(self.name)


class WishlistItem(models.Model):
    # wish lista rzeczy do kupienia / lista prezentów

    url = models.URLField(null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlist"

    def __str__ (self):
        return(self.name)
    

class AffiliateLink(models.Model):
    # wszelkie polecane rzeczy (z linkami affiliacyjnymi)
     
    url = models.URLField(null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Recomendations"
        verbose_name_plural = "Recomendations"

    def __str__ (self):
        return(self.name)