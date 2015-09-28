# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0012_auto_20150720_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='userId',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
