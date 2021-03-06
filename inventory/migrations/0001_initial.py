# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-07 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_id', models.CharField(blank=True, max_length=15, unique=True)),
                ('username', models.CharField(blank=True, max_length=15, unique=True)),
                ('password', models.CharField(blank=True, max_length=15, unique=True)),
                ('name', models.CharField(blank=True, max_length=15, unique=True)),
                ('surname', models.CharField(blank=True, max_length=15, unique=True)),
                ('mail', models.CharField(blank=True, max_length=30, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(blank=True, max_length=30)),
                ('db_host', models.CharField(blank=True, max_length=30)),
                ('db_user', models.CharField(blank=True, max_length=30)),
                ('db_pass', models.CharField(blank=True, max_length=30)),
                ('db_type', models.CharField(blank=True, max_length=30)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ClientInfo')),
            ],
            options={
                'ordering': ['db_name'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(blank=True, max_length=50)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ClientInfo')),
            ],
            options={
                'ordering': ['file_path'],
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_path', models.CharField(blank=True, max_length=50)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ClientInfo')),
            ],
            options={
                'ordering': ['folder_path'],
            },
        ),
    ]
