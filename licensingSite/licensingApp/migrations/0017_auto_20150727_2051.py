# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0016_auto_20150720_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='addOnDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isActivated', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='merchant',
            old_name='userId',
            new_name='reseller',
        ),
        migrations.RemoveField(
            model_name='addons',
            name='addOnType',
        ),
        migrations.RemoveField(
            model_name='addons',
            name='isActivated',
        ),
        migrations.RemoveField(
            model_name='addons',
            name='merchantID',
        ),
        migrations.AddField(
            model_name='addondetails',
            name='addOn',
            field=models.ForeignKey(to='licensingApp.addOns'),
        ),
        migrations.AddField(
            model_name='addondetails',
            name='merch',
            field=models.ForeignKey(to='licensingApp.merchant'),
        ),
    ]
