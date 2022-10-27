from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE) #associates User and Profile, now we can add fields:
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
