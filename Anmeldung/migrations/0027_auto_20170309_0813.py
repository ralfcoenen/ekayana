# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Anmeldung', '0026_event_bild_hoehe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='bild',
        ),
        migrations.RemoveField(
            model_name='event',
            name='bild_hoehe',
        ),
    ]
