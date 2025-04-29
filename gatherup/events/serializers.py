from rest_framework import serializers
from .models import Event, Like

class EventSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Shows username of the uploader
    is_liked = serializers.SerializerMethodField()  # Add the is_liked field

    class Meta:
        model = Event
        fields = '__all__'

    def get_is_liked(self, obj):
        user = self.context.get('request').user  # Get the currently authenticated user
        if user.is_authenticated:
            # Check if the user has liked the event
            return Like.objects.filter(user=user, event=obj).exists()
        return False
