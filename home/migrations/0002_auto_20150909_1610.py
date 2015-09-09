# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='site',
        ),
        migrations.RemoveField(
            model_name='game',
            name='site',
        ),
        migrations.RemoveField(
            model_name='library',
            name='site',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='site',
        ),
    ]
