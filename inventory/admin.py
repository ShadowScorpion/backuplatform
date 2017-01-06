from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect
from inventory.models import *

class DatabasesAdmin(admin.ModelAdmin):
    list_display = ('client', 'database', 'host', 'user', 'password')
    list_filter = ('client', 'database', 'host', 'user', 'password')

class DatabasesInline(admin.TabularInline):
    model = Databases

class ClientInfoAdmin(admin.ModelAdmin):
    list_display = ('client_id')
    list_filter = ('client_id')
    inlines = (DatabasesInline)


admin.site.register(ClientInfo, ClientInfoAdmin)
admin.site.register(Databases, DatabasesAdmin)
