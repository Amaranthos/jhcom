# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150821_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('video', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='/static/home\\img\\games\\thumbnails', default='/static/img\\placeholder.png')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('link', models.URLField()),
                ('thumbnail', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('thumbnail', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('video', models.URLField()),
                ('thumbnail', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='thumbnail',
            field=models.CharField(max_length=40),
        ),
    ]
