from rest_framework import serializers
from .models import Community
from .models import CommunityType
from .models import Parish

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['name', 'parish', 'type', 'lat', 'lng']

class CommunityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityType
        fields = ['name']

class ParishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parish
        fields = ['code', 'name']


