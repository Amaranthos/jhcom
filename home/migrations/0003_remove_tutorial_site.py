# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150909_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='site',
        ),
    ]
