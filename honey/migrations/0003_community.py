# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honey', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('descriptions', models.TextField()),
            ],
        ),
    ]
