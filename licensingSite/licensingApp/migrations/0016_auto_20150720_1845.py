# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0015_merchant_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='userId',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
