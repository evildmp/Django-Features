from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r"^request/(?P<slug>[-\w]+)/$", "features.views.request"),
    )