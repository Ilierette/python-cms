from django.contrib import admin
from .models import Banner, MenuItem, MainPageSections

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    change_list_template="settings\carousel.html"
    list_display = ["title", "subtitle", "active", "button_link"]
    actions_on_bottom = True
    actions_on_top = False
    fieldsets = [
        (
            None,
            {
                "fields": ["active", "image"],
            },
        ),
        (
            "Banner Info",
            {
                "fields": [("title", "subtitle"), ("button_text", "button_link")]
            }
        )
    ]

@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    change_list_template="settings\menu.html"
    actions_on_bottom = True
    actions_on_top = False
    list_display = ["name", "url", "parent", "order"]


@admin.register(MainPageSections)
class MainPageAdmin(admin.ModelAdmin):
    change_list_template="settings\section.html"
    actions_on_bottom = True
    actions_on_top = False
    list_display = ["title", "type", "button_link", "order"]
    fieldsets=[
        (
            None,
            {
                "fields": [("title", "subtitle"), ("button_text", "button_link"), ('type', 'order')]
            }
        )
    ]

