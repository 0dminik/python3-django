# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20170702_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(max_length=800),
        ),
    ]
