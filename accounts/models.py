from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES =(
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLES, default='user')
    description = models.TextField(blank=True, default='')
