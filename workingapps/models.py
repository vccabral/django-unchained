from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Database(models.Model):
    name = models.CharField(max_length=100)

class Framework(models.Model):
    name = models.CharField(max_length=100)

class SourceControl(models.Model):
    name = models.CharField(max_length=100)

class JenkinsServer(models.Model):
    url = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

class GitRepo(models.Model):
    url = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User)
    database = models.ForeignKey(Database)
    framework = models.ForeignKey(Framework)
    source_control = models.ForeignKey(SourceControl)
    jenkins_server = models.ForeignKey(JenkinsServer)
    git_repo = models.ForeignKey(GitRepo)
