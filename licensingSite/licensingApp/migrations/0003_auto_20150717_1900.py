# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0002_auto_20150716_1631'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='license',
            new_name='addOns',
        ),
        migrations.RenameField(
            model_name='addons',
            old_name='licenseType',
            new_name='addOnType',
        ),
    ]
