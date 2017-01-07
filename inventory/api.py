from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from rest_framework import permissions
from inventory.serializer import ClientInfoSerializer, DatabaseSerializer, FileSerializer, FolderSerializer
from inventory.models import ClientInfo, Database, File, Folder


class ClientInfoList(ListCreateAPIView):
    """ List all servers, or create a new server.
    """
    queryset = ClientInfo.objects.all()
    serializer_class = ClientInfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ClientInfoDetail(RetrieveUpdateDestroyAPIView):
    """ Get, update or delete a specific server.
    """
    queryset = ClientInfo.objects.all()
    serializer_class = ClientInfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DatabaseList(ListCreateAPIView):
    """ List all servers, or create a new server.
    """
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DatabaseDetail(RetrieveUpdateDestroyAPIView):
    """ Get, update or delete a specific server.
    """
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class FileList(ListCreateAPIView):
    """ List all servers, or create a new server.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class FileDetail(RetrieveUpdateDestroyAPIView):
    """ Get, update or delete a specific server.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class FolderList(ListCreateAPIView):
    """ List all servers, or create a new server.
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class FolderDetail(RetrieveUpdateDestroyAPIView):
    """ Get, update or delete a specific server.
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
