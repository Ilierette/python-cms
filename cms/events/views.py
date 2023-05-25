from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from events.models import Event
from events.serializers import EventSerializer

@csrf_exempt
def events_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many="True")
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def event_detail(request, pk):
    try: 
        event = Event.objects.get(pk=pk)

    except Event.DoesNotExist:
        return HttpResponse(status=404)    
    
    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)
