from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

# View to list and create events (API)
class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View to get, update, or delete a specific event (API)
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAuthenticated]  # Ensure users are logged in to edit or delete events

# Home page - login required
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'events/Home.html')

# Events page - login required
@login_required(login_url='/accounts/login/')
def events_page(request):
    return render(request, 'events/events.html')
