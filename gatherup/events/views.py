from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import EventSerializer
from .forms import EventForm
from django.http import JsonResponse
from .models import Event, Like
from django.shortcuts import get_object_or_404

# View to list all events
class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
     

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# View get a specific event
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'events/Home.html')

@login_required(login_url='/accounts/login/')
def events_page(request):
    return render(request, 'events/events.html')





@login_required(login_url='/accounts/login/')
def upload_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.host_profile_name = request.user.username
            event.save()
            return redirect('events-page')  
    else:
        form = EventForm()
    return render(request, 'events/upload.html', {'form': form})





@login_required(login_url='/accounts/login/')
def like_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

   
    like = Like.objects.filter(user=user, event=event).first()
    if like:
        
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
 
    
    return JsonResponse({
        'like_count': like_count
    })


#view only the users created events
class MyEvents(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
       
        return Event.objects.filter(user=self.request.user)
    

class DeleteEventView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


    def get_queryset(self):
      
        return Event.objects.filter(user=self.request.user)
    
@login_required(login_url='/accounts/login/')
def my_events(request):
    return render(request, 'events/My_Events.html')
