# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20161008_1239'),
        ('clients', '0003_auto_20161021_0922'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='client',
            unique_together=set([('company', 'code'), ('company', 'id_num')]),
        ),
    ]
