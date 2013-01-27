from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    public_key = models.CharField(max_length=200)
    aws_secret_key = models.CharField(max_length=200)
    
