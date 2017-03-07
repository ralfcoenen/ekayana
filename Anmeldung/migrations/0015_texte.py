# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 10:29
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anmeldung', '0014_auto_20170306_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='texte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bereich', models.CharField(max_length=50)),
                ('headertext', models.CharField(max_length=50)),
                ('langtext', ckeditor.fields.RichTextField()),
            ],
        ),
    ]