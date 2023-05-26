from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("events/", views.events_list),
    path("events/event/<int:pk>", views.event_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)