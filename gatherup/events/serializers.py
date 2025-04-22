from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Shows username of the uploader

    class Meta:
        model = Event
        fields = '__all__'
