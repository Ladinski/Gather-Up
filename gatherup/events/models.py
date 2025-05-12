import os
from django.db import models
from accounts.models import CustomUser 

class Event(models.Model):
    EVENT_TYPES = (
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('webinar', 'Webinar'),
        ('networking', 'Networking'),
        ('meetup', 'Meetup'),
        ('expo', 'Expo'),
        ('trade_show', 'Trade Show'),
        ('product_launch', 'Product Launch'),
        ('fundraiser', 'Fundraiser'),
        ('social', 'Social'),
        ('party', 'Party'),
        ('performance', 'Performance'),
        ('exhibition', 'Exhibition'),
        ('retreat', 'Retreat'),
        ('panel', 'Panel'),
        ('class', 'Class'),
        ('festival', 'Festival'),
        ('meeting', 'Meeting'),
        ('sports', 'Sports'),
        ('volunteering', 'Volunteering'),
        ('holiday', 'Holiday'),
    )

    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=EVENT_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    host_profile_name = models.CharField(max_length=30)
    date_time = models.DateTimeField()  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    likes = models.PositiveIntegerField(default=0)
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


from django.db import models
from django.conf import settings
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')