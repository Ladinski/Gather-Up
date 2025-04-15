from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from django.shortcuts import render

# View to list all events
class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# View to get a specific event
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def home(request):
    return render(request, 'events/Home.html')

def events_page(request):
    return render(request, 'events/events.html')