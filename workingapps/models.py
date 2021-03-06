from django.db import models
from django.contrib.auth.models import User

class BaseNamedModel(models.Model):
    class Meta:
        abstract = True
    __str__ = lambda self: self.name

class BaseUrledModel(models.Model):
    class Meta:
        abstract = True
    __str__ = lambda self: self.url

class Database(BaseNamedModel):
    name = models.CharField(max_length=100)
		
class Framework(BaseNamedModel):
    name = models.CharField(max_length=100)

class SourceControl(BaseNamedModel):
    name = models.CharField(max_length=100)

class JenkinsServer(BaseUrledModel):
    url = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=False)
    __str__ = lambda self: str(self.pk)

class GitRepo(BaseUrledModel):
    url = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=False)
    __str__ = lambda self: str(self.pk)
    
class ProductionServer(BaseUrledModel):
    url = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=False)

class ProductionDatabase(BaseUrledModel):
    url = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=False)
    
class Project(BaseNamedModel):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User)
    database = models.ForeignKey(Database)
    framework = models.ForeignKey(Framework)
    source_control = models.ForeignKey(SourceControl)
    jenkins_server = models.ForeignKey(JenkinsServer)
    git_repo = models.ForeignKey(GitRepo)
    production_server = models.ForeignKey(ProductionServer)
    production_database = models.ForeignKey(ProductionDatabase)
    status = lambda self: all([self.jenkins_server.is_active,self.git_repo.is_active, self.production_server.is_active, self.production_database.is_active])