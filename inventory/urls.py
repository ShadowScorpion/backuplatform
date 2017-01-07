#from django.conf.urls import include, patterns, url
from inventory import models
from django.views.generic.detail import DetailView

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#)
