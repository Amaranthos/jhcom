# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='link',
            new_name='links',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='link',
            new_name='links',
        ),
        migrations.RenameField(
            model_name='library',
            old_name='link',
            new_name='links',
        ),
        migrations.RenameField(
            model_name='tool',
            old_name='link',
            new_name='links',
        ),
    ]
