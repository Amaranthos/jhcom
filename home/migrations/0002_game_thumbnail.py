# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='thumbnail',
            field=models.ImageField(default='c:\\Users\\Josh\\Desktop\\Projects\\Web\\static\\root\\img\\placeholder.png', upload_to='img/games/thumbnails/'),
        ),
    ]
