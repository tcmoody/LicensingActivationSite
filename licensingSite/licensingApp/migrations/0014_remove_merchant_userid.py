# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0013_auto_20150720_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='userId',
        ),
    ]
