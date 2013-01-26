from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Database(models.Model):
    name = models.CharField(max_length=100)
    __str__ = lambda self: self.name
		
class Framework(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
	    return self.name

class SourceControl(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
	    return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User)
    database = models.ForeignKey(Database)
    framework = models.ForeignKey(Framework)
    source_control = models.ForeignKey(SourceControl)
    def __str__(self):
	    return self.name

