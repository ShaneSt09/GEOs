from rest_framework import serializers
from .models import CommunityType
from .models import Parish
from .models import Community

class CommunityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommunityType
        fields=['name']

class ParishSerializer(serializers.ModelSerializer):
    class Meta:
        model=Parish
        fields=['name', 'code']

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Community
        fields=['name', 'parish', 'type']

