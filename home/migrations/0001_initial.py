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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True, default=models.CharField(unique=True, max_length=50))),
                ('video', models.URLField()),
                ('thumbnail', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'App',
                'verbose_name_plural': 'Apps',
            },
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Art',
                'verbose_name_plural': 'Art',
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Contributor',
                'verbose_name_plural': 'Contributors',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True, default=models.CharField(unique=True, max_length=50))),
                ('video', models.URLField()),
                ('thumbnail', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(to='home.Contributor')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True, default=models.CharField(unique=True, max_length=50))),
                ('thumbnail', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(to='home.Contributor')),
            ],
            options={
                'verbose_name': 'Library',
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('thumbnail', models.CharField(max_length=40)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True, default=models.CharField(unique=True, max_length=50))),
                ('video', models.URLField()),
                ('thumbnail', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(to='home.Contributor')),
                ('links', models.ManyToManyField(to='home.Link')),
            ],
            options={
                'verbose_name': 'Tool',
                'verbose_name_plural': 'Tools',
            },
        ),
        migrations.AddField(
            model_name='library',
            name='links',
            field=models.ManyToManyField(to='home.Link'),
        ),
        migrations.AddField(
            model_name='game',
            name='links',
            field=models.ManyToManyField(to='home.Link'),
        ),
        migrations.AddField(
            model_name='app',
            name='contributors',
            field=models.ManyToManyField(to='home.Contributor'),
        ),
        migrations.AddField(
            model_name='app',
            name='links',
            field=models.ManyToManyField(to='home.Link'),
        ),
    ]
