# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0009_merchant_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='userId',
        ),
    ]
