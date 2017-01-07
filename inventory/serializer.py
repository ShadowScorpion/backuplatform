from inventory.models import ClientInfo, Database, File, Folder
from rest_framework import serializers

class ClientInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientInfo
        fields = ('id', 'access_id', 'username', 'password', 'name', 'surname', 'mail', 'phone')


class DatabaseSerializer(serializers.ModelSerializer):

    client_id = serializers.SlugRelatedField(queryset=ClientInfo.objects.all(),
                                           slug_field='access_id')

    class Meta:
        model = Database
        fields = ('id', 'client_id', 'db_name', 'db_host', 'db_user', 'db_pass', 'db_type')

class FileSerializer(serializers.ModelSerializer):

    client_id = serializers.SlugRelatedField(queryset=ClientInfo.objects.all(),
                                           slug_field='access_id')

    class Meta:
        model = File
        fields = ('id', 'client_id', 'file_path')


class FolderSerializer(serializers.ModelSerializer):

    client_id = serializers.SlugRelatedField(queryset=ClientInfo.objects.all(),
                                           slug_field='access_id')

    class Meta:
        model = Folder
        fields = ('id', 'client_id', 'folder_path')
