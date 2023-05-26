from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from links.models import Event, SocialMediaLink, WishlistItem, AffiliateLink
from links.serializers import EventSerializer, SocialMediaSerializer, WishListSerializer, AffiliateSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def events_list(request, format=None):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def event_detail(request, pk, format=None):
    try: 
        event = Event.objects.get(pk=pk)

    except Event.DoesNotExist:
        return HttpResponse(status=404)    
    
    serializer = EventSerializer(event)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def media_list(request, format=None):
    link = SocialMediaLink.objects.all()
    serializer = SocialMediaSerializer(link, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def wish_list(request, format=None):
    link = WishlistItem.objects.all()
    serializer = WishListSerializer(link, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def wish_detail(request, pk, format=None):
    try: 
        link = WishlistItem.objects.get(pk=pk)

    except Event.DoesNotExist:
        return HttpResponse(status=404)    
    
    serializer = WishListSerializer(link)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def affiliate_list(request, format=None):
    link = AffiliateLink.objects.all()
    serializer = AffiliateSerializer(link, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def affiliate_detail(request, pk, format=None):
    try: 
        wish = AffiliateLink.objects.get(pk=pk)

    except Event.DoesNotExist:
        return HttpResponse(status=404)    
    
    serializer = AffiliateSerializer(wish)
    return JsonResponse(serializer.data)