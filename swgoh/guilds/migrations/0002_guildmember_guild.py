# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildmember',
            name='guild',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guilds.Guild'),
            preserve_default=False,
        ),
    ]
