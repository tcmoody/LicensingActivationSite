# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='license',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('licenseType', models.CharField(max_length=100)),
                ('isActivated', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='Merchants',
            new_name='merchant',
        ),
        migrations.RemoveField(
            model_name='licenses',
            name='merchantID',
        ),
        migrations.DeleteModel(
            name='Licenses',
        ),
        migrations.AddField(
            model_name='license',
            name='merchantID',
            field=models.ManyToManyField(to='licensingApp.merchant'),
        ),
    ]
