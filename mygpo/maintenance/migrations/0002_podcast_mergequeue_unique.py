# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 18:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0037_index_podcast_lastupdate'),
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mergequeueentry',
            unique_together=set([('podcast',)]),
        ),
    ]