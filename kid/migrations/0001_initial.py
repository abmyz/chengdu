# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Qingyang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField(blank=True, db_column='_id', max_length=255, null=True)),
                ('field_area', models.CharField(blank=True, db_column='\ufeffarea', max_length=255, null=True)),
                ('no', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('whether_public_welfare', models.CharField(blank=True, db_column='Whether public welfare', max_length=255, null=True)),
                ('nature', models.CharField(blank=True, max_length=255, null=True)),
                ('grade', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('lng', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'qingyang',
                'managed': False,
            },
        ),
    ]