# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0025_auto_20161007_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='cubic_meters_warning',
            field=models.FloatField(blank=True, help_text='Selecionou "Enviar email". Tem de selecionar um valor'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='power_warning',
            field=models.FloatField(blank=True, help_text='Selecionou "Enviar email". Tem de selecionar um valor'),
        ),
    ]