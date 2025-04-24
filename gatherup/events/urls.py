from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events_page, name='events-page'),  # new
    path('upload/', views.upload_event, name='upload_event'),
    path('api/events/', views.EventListView.as_view(), name='event-list'),
    path('api/events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
]
