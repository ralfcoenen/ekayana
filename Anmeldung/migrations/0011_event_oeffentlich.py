# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anmeldung', '0010_event_kurzbeschreibung'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='oeffentlich',
            field=models.BooleanField(default='True'),
        ),
    ]
