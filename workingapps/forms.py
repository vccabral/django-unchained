from django.forms import ModelForm
from workingapps.models import Project

class ProjectCreateForm(ModelForm):
	class Meta:
		exclude = ('admin')
		model = Project
