# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todomodel_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]