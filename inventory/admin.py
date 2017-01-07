from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect
from inventory.models import *

class ClientInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'access_id', 'username', 'password', 'name', 'surname', 'mail', 'phone')
    list_filter = ('id', 'access_id', 'username')

class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'db_name', 'db_host', 'db_user', 'db_pass', 'db_type')
    list_filter = ('id', 'client_id', 'db_type')
 
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'file_path')
    list_filter = ('id', 'client_id', 'file_path')

class FolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'folder_path')
    list_filter = ('id', 'client_id', 'folder_path')

admin.site.register(ClientInfo, ClientInfoAdmin)
admin.site.register(Database, DatabaseAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Folder, FolderAdmin)
