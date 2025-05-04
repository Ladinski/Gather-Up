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
            event.host_profile_name = request.user.username
            event.save()
            return redirect('events-page')  # or wherever you want to go after upload
    else:
        form = EventForm()
    return render(request, 'events/upload.html', {'form': form})


from django.http import JsonResponse
from .models import Event, Like
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def like_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

    # Check if this user already liked this event
    like = Like.objects.filter(user=user, event=event).first()
    if like:
        # If already liked, delete the like (unlike)
        like.delete()
        like_count = Like.objects.filter(event=event).count()
        event.likes = like_count
        event.save()  
        
        return JsonResponse({'message': 'Event unliked successfully!'})
    else:
        Like.objects.create(user=user, event=event)

    like_count = Like.objects.filter(event=event).count()
    event.likes = like_count
    event.save()  
    # Else, create a new Like
    
    return JsonResponse({
        'like_count': like_count
    })



class MyEvents(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        # Filter events by the currently logged-in user
        return Event.objects.filter(user=self.request.user)
    

class DeleteEventView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


    def get_queryset(self):
        # Only allow the user to delete their own events
        return Event.objects.filter(user=self.request.user)
    
@login_required(login_url='/accounts/login/')
def my_events(request):
    return render(request, 'events/My_Events.html')
