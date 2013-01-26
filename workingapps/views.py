from django.shortcuts import render_to_response
from django.template.context import RequestContext
from workingapps.forms import ProjectCreateForm

def create(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            return render_to_response('projects.html', context_instance=RequestContext(request))
    else: 
        form = ProjectCreateForm()
    return render_to_response('project_create.html', {'form': form} , context_instance=RequestContext(request))

def index(request):
    return render_to_response('projects.html', context_instance=RequestContext(request))
