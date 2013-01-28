from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from workingapps.forms import ProjectCreateForm
from workingapps.models import Project, JenkinsServer, GitRepo, ProductionServer, ProductionDatabase

def create(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            newproject = form.save(commit=False)
            newproject.admin = request.user
            newproject.jenkins_server = JenkinsServer.objects.create(is_active=False)
            newproject.git_repo = GitRepo.objects.create(is_active=False)
            newproject.production_server = ProductionServer.objects.create(is_active=False)
            newproject.production_database = ProductionDatabase.objects.create(is_active=False)
            newproject.save()
            return redirect("project_index")
    else: 
        form = ProjectCreateForm()
    return render_to_response('project_create.html', {'form': form} , context_instance=RequestContext(request))

def index(request):
    projects = Project.objects.filter(admin=request.user)
    return render_to_response('projects.html', locals(), context_instance=RequestContext(request))
