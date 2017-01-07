from django.db import models

class ClientInfo(models.Model):
#    def __unicode__(self):
#        return unicode(self.id)

    def __str__(self):
        return self.access_id

    class Meta:
        ordering = ['id']

    access_id = models.CharField(max_length=15, unique=True, blank=True)
    username = models.CharField(max_length=15, unique=True, blank=True)
    password = models.CharField(max_length=15, unique=True, blank=True)
    name = models.CharField(max_length=15, unique=True, blank=True)
    surname = models.CharField(max_length=15, unique=True, blank=True)
    mail = models.CharField(max_length=30, unique=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, blank=True)

class Database(models.Model):
    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        ordering = ['db_name']
#        unique_together = (('client', 'database'),)

    client_id = models.ForeignKey(ClientInfo)
    db_name = models.CharField(max_length=30, blank=True)
    db_host = models.CharField(max_length=30, blank=True)
    db_user = models.CharField(max_length=30, blank=True)
    db_pass = models.CharField(max_length=30, blank=True)
    db_type = models.CharField(max_length=30, blank=True)

class File(models.Model):
    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        ordering = ['file_path']

    client_id = models.ForeignKey(ClientInfo)
    file_path = models.CharField(max_length=50, blank=True)

class Folder(models.Model):
    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        ordering = ['folder_path']

    client_id = models.ForeignKey(ClientInfo)
    folder_path = models.CharField(max_length=50, blank=True)
