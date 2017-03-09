# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anmeldung', '0018_auto_20170307_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Veranstaltung', 'verbose_name_plural': 'Veranstaltungen'},
        ),
        migrations.AlterModelOptions(
            name='teilnehmer',
            options={'verbose_name': 'Teilnehmer', 'verbose_name_plural': 'Teilnehmer'},
        ),
        migrations.AlterModelOptions(
            name='texte',
            options={'verbose_name': 'Texte', 'verbose_name_plural': 'Texte'},
        ),
        migrations.AddField(
            model_name='event',
            name='bild',
            field=models.ImageField(null=True, upload_to='bilder'),
        ),
        migrations.AlterField(
            model_name='event',
            name='oeffentlich',
            field=models.BooleanField(default=True, verbose_name='Öffentliche Veranstaltung bzw. noch Plätze frei'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registrationdeadline',
            field=models.DateField(null=True, verbose_name='Sichtbar bis einschl.'),
        ),
        migrations.AlterField(
            model_name='teilnehmer',
            name='strasse',
            field=models.CharField(max_length=60, verbose_name='Straße und Hausnummer'),
        ),
        migrations.AlterField(
            model_name='texte',
            name='headertext',
            field=models.CharField(max_length=50, verbose_name='Überschrift'),
        ),
    ]
