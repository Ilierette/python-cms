from django.contrib import admin
from .models import Event, SocialMediaLink, WishlistItem

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    change_list_template='admin\event_description.html'
    actions_on_bottom = True
    actions_on_top = False
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