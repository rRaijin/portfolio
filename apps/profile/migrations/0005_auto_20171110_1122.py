# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_languageskills_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='interest_logotype',
            field=models.ImageField(blank=True, null=True, upload_to='work_images/'),
        ),
        migrations.AlterField(
            model_name='languageskills',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
