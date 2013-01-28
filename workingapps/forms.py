from django.forms import ModelForm
from workingapps.models import Project

class ProjectCreateForm(ModelForm):
	class Meta:
		exclude = ('admin','jenkins_server','git_repo','production_server','production_database')
		model = Project
