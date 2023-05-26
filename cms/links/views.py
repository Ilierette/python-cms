from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from links.models import Event
from links.serializers import EventSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def events_list(request, format=None):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many="True")
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def event_detail(request, pk, format=None):
    try: 
        event = Event.objects.get(pk=pk)

    except Event.DoesNotExist:
        return HttpResponse(status=404)    
    
    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)
