from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Event, Like
from .forms import EventForm
# Create your tests here.

User  = get_user_model()

class EventTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.event = Event.objects.create(title='Test Event', description='Test Description', user=self.user)

    def test_event_list_view(self):
        response = self.client.get(reverse('event-list')) 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_detail_view(self):
        response = self.client.get(reverse('event-detail', args=[self.event.id])) 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_create_view(self):
        response = self.client.post(reverse('event-create'), {
            'title': 'New Event',
            'description': 'New Description',
            'date': '2023-10-10',  
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Event.objects.filter(title='New Event').exists())

    def test_event_like_view(self):
        response = self.client.post(reverse('like-event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['like_count'], 1)

        
        response = self.client.post(reverse('like-event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Event unliked successfully!')

    def test_my_events_view(self):
        response = self.client.get(reverse('my-events')) 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Events')

    def test_event_delete_view(self):
        response = self.client.delete(reverse('event-delete', args=[self.event.id]))  
        self.assertEqual(response.status_code, 204)  
        self.assertFalse(Event.objects.filter(id=self.event.id).exists())

    def test_upload_event_view(self):
        response = self.client.get(reverse('upload-event'))  
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('upload-event'), {
            'title': 'Upload Event',
            'description': 'Upload Description',
            'date': '2023-10-10',  
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Event.objects.filter(title='Upload Event').exists())
