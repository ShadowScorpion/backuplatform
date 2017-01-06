from django.db import models

class ClientInfo(models.Model):
    def __unicode__(self):
        return unicode(self.client_id)

    class Meta:
        ordering = ['client_id']

    client_id = models.CharField(max_length=15, unique=True, blank=True)

class Databases(models.Model):
    def __unicode__(self):
        return unicode(self.database)

    class Meta:
        ordering = ['database']
        unique_together = (('client', 'database'),)

    client = models.ForeignKey(ClientInfo)
    database = models.CharField(max_length=15, blank=True)
    host = models.CharField(max_length=15, blank=True)
    user = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=15, blank=True)
