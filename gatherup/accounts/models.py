from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # By default, AbstractUser already includes username and password, 
    # so you don't need to add them explicitly again.
    pass