from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events_page, name='events-page'),  # new
    path('upload/', views.upload_event, name='upload_event'),
    path('my-events/', views.my_events, name='my-events'),
    path('api/events/', views.EventListView.as_view(), name='event-list'),
    path('api/myevents/', views.MyEvents.as_view(), name='myevent-list'),
    path('api/events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('api/delete-event/<int:pk>/', views.DeleteEventView.as_view(), name='delete-event'),
    path('events/like/<int:event_id>/', views.like_event, name='like-event'),
]
