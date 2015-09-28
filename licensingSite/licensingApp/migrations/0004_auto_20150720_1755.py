# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0003_auto_20150717_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchant',
            old_name='name',
            new_name='merchantName',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='UserID',
        ),
    ]
