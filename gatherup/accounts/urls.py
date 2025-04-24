from django.urls import path
from . import views
from .views import profile_view, logout_view
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # <-- Add this
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('password_change/', login_required(PasswordChangeView.as_view(success_url='/')), name='password_change'),
]