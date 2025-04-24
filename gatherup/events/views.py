from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from .forms import EventForm

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


# events/views.py


@login_required(login_url='/accounts/login/')
def upload_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.likes = 0
            event.host_profile_name = request.user.username
            event.save()
            return redirect('events-page')  # or wherever you want to go after upload
    else:
        form = EventForm()
    return render(request, 'events/upload.html', {'form': form})

