from django.contrib import admin
from .models import AffiliateLink, Event, SocialMediaLink, WishlistItem

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    change_list_template="links\event_description.html"
    actions_on_bottom = True
    actions_on_top = False
    list_display=["name","event_date"]
    fieldsets=[
        (
            None,
            {
                "fields":[("name","url")],
            }
        ),
        (
            "Dates",
            {
                "fields":[("pub_date","event_date")]
            }
        )
    ]

@admin.register(SocialMediaLink)
class SocialMediaAdmin(admin.ModelAdmin):
    change_list_template="links\social_description.html"
    actions_on_bottom = True
    actions_on_top = False
    list_display=["name", "url"]
    fieldsets=[
        (
            None,
            {
                "fields": [("name","url")]
            }
        )
    ]



@admin.register(WishlistItem)
class WishlistAdmin(admin.ModelAdmin):
    change_list_template="links\wishlist_description.html"
    actions_on_bottom = True
    actions_on_top = False
    list_display=["name", "url", "description"]
    fieldsets=[
        (
            None,
            {
                "fields": [("name","url")]
            }
        ),
        (
            "Description",
            {
                "fields": ["description"]
            }
        )
    ]

@admin.register(AffiliateLink)
class AffiliateAdmin(admin.ModelAdmin):
    change_list_template="links\description.html"
    actions_on_bottom = True
    actions_on_top = False
    list_display=["name", "url", "description"]
    fieldsets=[
        (
            None,
            {
                "fields": [("name","url")]
            }
        ),
        (
            "Description",
            {
                "fields": ["description"]
            }
        )
    ]