# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_auto_20160602_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
