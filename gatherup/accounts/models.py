from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # By default AbstractUser includes username and password
    pass