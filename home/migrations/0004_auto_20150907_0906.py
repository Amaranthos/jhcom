# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='app',
            name='thumbnail',
            field=models.ImageField(upload_to='home/img/apps/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='game',
            name='thumbnail',
            field=models.ImageField(upload_to='home/img/games/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='library',
            name='thumbnail',
            field=models.ImageField(upload_to='home/img/libraries/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='site',
            name='thumbnail',
            field=models.ImageField(upload_to='home/img/sites/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='thumbnail',
            field=models.ImageField(upload_to='home/img/tools/thumbnails/'),
        ),
    ]
