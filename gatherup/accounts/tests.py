from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your tests here.
class AccountViewsTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.email = 'testuser@example.com'
        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('home'))

        # Test invalid login
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Please enter a correct username and password.')

    def test_signup_view(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('home'))

        # Test existing username
        response = self.client.post(reverse('signup'), {
            'username': self.username,
            'email': 'anotheremail@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'Username already exists')

    def test_profile_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_logout_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, '/accounts/login/')
