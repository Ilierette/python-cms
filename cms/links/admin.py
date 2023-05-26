from django.contrib import admin
from .models import Event, SocialMediaLink, WishlistItem

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=["title","event_date"]
    fieldsets=[
        (
            None,
            {
                'fields':['title',('pub_date','event_date'),'url'],
            }
        ),
        (
            'Optional',
            {
                'classes':['collapse'],
                'fields':['description']
            }
        )
    ]
    pass


admin.site.register(SocialMediaLink)
admin.site.register(WishlistItem)