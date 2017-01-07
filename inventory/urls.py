from django.conf.urls import include, url
from django.views.generic.detail import DetailView

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

from inventory.models import *
from inventory.api import *
from inventory.serializer import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^api/clientinfo/$', ClientInfoList.as_view(),
            name='clientinfo_list'),
    url(r'^api/clientinfo/(?P<pk>[0-9]+)$', ClientInfoDetail.as_view(),
            name='clientinfo_detail'),
    url(r'^api/database/$', DatabaseList.as_view(),
            name='database_list'),
    url(r'^api/database/(?P<pk>[0-9]+)$', DatabaseDetail.as_view(),
            name='database_detail'),
    url(r'^api/folder/$', FolderList.as_view(),
            name='folder_list'),
    url(r'^api/folder/(?P<pk>[0-9]+)$', FolderDetail.as_view(),
            name='folder_detail'),
    url(r'^api/file/$', FileList.as_view(),
            name='file_list'),
    url(r'^api/file/(?P<pk>[0-9]+)$', FileDetail.as_view(),
            name='file_detail'),
]







#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#)
