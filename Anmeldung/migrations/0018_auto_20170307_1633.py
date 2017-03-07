# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 15:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anmeldung', '0017_auto_20170307_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='texte',
            name='datepublished',
        ),
        migrations.AddField(
            model_name='texte',
            name='datepublishedend',
            field=models.DateField(default=datetime.date.today, verbose_name='Veröffentlichung bis'),
        ),
        migrations.AddField(
            model_name='texte',
            name='datepublishedstart',
            field=models.DateField(default=datetime.date.today, verbose_name='Veröffentlichung von'),
        ),
    ]