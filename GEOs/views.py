from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CommunityType, Parish, Community
from .serializer import CommunityTypeSerializer, ParishSerializer, CommunitySerializer

# Create your views here.

#GET methods for API endpoints here
@api_view(['GET'])
def getCommunityType(request):
    communitytype = CommunityType.objects.all()
    ctserializer = CommunityTypeSerializer(communitytype, many=True)
    return Response(ctserializer.data)

@api_view(['GET'])
def getParish(request):
    parish = Parish.objects.all()
    pserializer = ParishSerializer(parish, many=True)
    return Response(pserializer.data)

@api_view(['GET'])
def getCommunity(request):
    community = Community.objects.all()
    cserializer = CommunitySerializer(community, many=True)
    return Response(cserializer.data)

#POST methods for API endpoints here

@api_view(['POST'])
def postCommunityType(request):
    ctserializer = CommunityTypeSerializer(data=request.data)
    if ctserializer.is_valid():
        ctserializer.save()
    return Response(ctserializer.data)

@api_view(['POST'])
def postParish(request):
    pserializer = ParishSerializer(data=request.data)
    if pserializer.is_valid():
        pserializer.save()
    return Response(pserializer.data)

@api_view(['POST'])
def postCommunity(request):
    cserializer = CommunitySerializer(data=request.data)
    if cserializer.is_valid():
        cserializer.save()
    return Response(cserializer.data)