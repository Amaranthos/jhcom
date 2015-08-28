# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True, default=models.CharField(unique=True, max_length=50))),
                ('video', models.URLField()),
                ('thumbnail', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True, default=models.CharField(unique=True, max_length=50))),
                ('video', models.URLField()),
                ('thumbnail', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('contributors', models.ManyToManyField(to='home.Contributor')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True, default=models.CharField(unique=True, max_length=50))),
                ('thumbnail', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('contributors', models.ManyToManyField(to='home.Contributor')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('thumbnail', models.CharField(max_length=40)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True, default=models.CharField(unique=True, max_length=50))),
                ('video', models.URLField()),
                ('thumbnail', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('contributors', models.ManyToManyField(to='home.Contributor')),
                ('link', models.ManyToManyField(to='home.Link')),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='link',
            field=models.ManyToManyField(to='home.Link'),
        ),
        migrations.AddField(
            model_name='game',
            name='link',
            field=models.ManyToManyField(to='home.Link'),
        ),
        migrations.AddField(
            model_name='app',
            name='contributors',
            field=models.ManyToManyField(to='home.Contributor'),
        ),
        migrations.AddField(
            model_name='app',
            name='link',
            field=models.ManyToManyField(to='home.Link'),
        ),
    ]
