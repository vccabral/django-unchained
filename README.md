DjangoTemplate
==============
forked from
pinax-project-account
=====================

a starter project the incorporates account features from django-user-accounts


Usage:

    django-admin.py startproject --template=https://github.com/vccabral/DjangoTemplate/zipball/master <project_name>

Example:

    rm -rf BangGangOfFour/
    django-admin.py startproject --template=https://github.com/vccabral/DjangoTemplate/zipball/master BangGangOfFour
    cd BangGangOfFour/
    virtualenv localpython
    source localpython/bin/activate
    pip install -r requirements.txt
    //edit your settings.py to reflect your database settings or use the default sql lite settings. 
    python manage.py syncdb
    python manage.py runserver

THENN.....start using south for db migrations
    python manage.py schemamigration publicface --initial

THENNNN....
Edit the {% block navbox %} in ./publicface/templates/site_base_private.html
{% block nav %}
<ul class="nav">
    <li id="tab_fifth">
        <a href="#">Link Me Here</a>
    </li>
</ul>
{% endblock %}

And create extra replicas of /publicface/template/publichome.html with the following block in them.
{% extends "site_base_private.html" %}
{% block head_title %}{% trans "Welcome" %}{% endblock %}
{% block body %}
{% endblock %}

THEN....make db schema change and follow the south documentation.....
http://south.readthedocs.org/en/latest/tutorial/part1.html
