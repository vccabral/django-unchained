from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', 'workingapps.views.index', name='project_index'),
                       )