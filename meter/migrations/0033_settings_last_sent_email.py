# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0032_auto_20161009_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='last_sent_email',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
