# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honey', '0003_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='email',
            field=models.CharField(default=333, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='password',
            field=models.CharField(default=333, max_length=32),
            preserve_default=False,
        ),
    ]
