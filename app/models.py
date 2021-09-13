from django.db import models
from django.urls import reverse
import os

from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass
