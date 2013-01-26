from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.simple import direct_to_template, redirect_to
from django.db.models import get_models, get_app
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin

def autoregister(*app_list):
    for app_name in app_list:
        app_models = get_app(app_name)
        for model in get_models(app_models):
            try:
                admin.site.register(model)
            except AlreadyRegistered:
                pass

autoregister("publicface","workingapps")
admin.autodiscover()


urlpatterns = patterns("",
    url(r"^$", redirect_to, {"url": "/home/"}, name="home_redirect"),
    url(r"^home/$", direct_to_template, {"template": "homepage.html"}, name="home"),
    url(r'^accounts/login/$',redirect_to, {"url": "/account/login/"}),
    url(r"^user/", include("publicface.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
