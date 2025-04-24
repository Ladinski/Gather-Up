from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user', 'likes', 'host_profile_name']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
