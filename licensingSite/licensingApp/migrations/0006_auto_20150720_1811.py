# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0005_auto_20150720_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='merchantName',
            field=models.CharField(max_length=100),
        ),
    ]
