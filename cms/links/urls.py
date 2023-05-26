from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("events/", views.events_list),
    path("events/event/<int:pk>", views.event_detail),
    path("social-links/", views.media_list),
    path("wishlist/", views.wish_list),
    path("wishlist/item/<int:pk>", views.wish_detail),
    path("recomendation-list/", views.affiliate_list),
    path("recomendation-list/item/<int:pk>", views.affiliate_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)