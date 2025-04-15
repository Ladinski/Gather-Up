import os
from django.db import models

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
    likes = models.IntegerField(default=0)
    date_time = models.DateTimeField()  # New field for event date and time


    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
