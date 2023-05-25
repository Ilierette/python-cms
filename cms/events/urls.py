from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.events_list),
    path("event/<int:pk>", views.event_detail),
]