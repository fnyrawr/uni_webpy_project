from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLES = [
        ('SU', 'superuser'),
        ('CS', 'customer service'),
        ('CU', 'customer'),
        ('BP', 'business partner'),
    ]
    email = models.EmailField(blank=True, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank = True, null = True)
    role = models.CharField(max_length=2,
                            choices=ROLES,
							default='CU',
                            )
