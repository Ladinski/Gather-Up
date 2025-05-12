from rest_framework import serializers
from .models import Event, Like

class EventSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  
    is_liked = serializers.SerializerMethodField()  

    class Meta:
        model = Event
        fields = '__all__'

    def get_is_liked(self, obj):
        user = self.context.get('request').user  
        if user.is_authenticated:
           
            return Like.objects.filter(user=user, event=obj).exists()
        return False
