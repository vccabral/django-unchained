from django.shortcuts import render_to_response
from django.template.context import RequestContext
from workingapps.models import Project

def index(request):
    projects = Project.objects.filter(admin=request.user)
    return render_to_response('projects.html', locals(), context_instance=RequestContext(request))
