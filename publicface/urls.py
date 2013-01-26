from django.conf.urls.defaults import patterns, url
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.simple import direct_to_template, redirect_to
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
                       url(r'^$', 'publicface.views.index', name='publicface_index'),
                       )
