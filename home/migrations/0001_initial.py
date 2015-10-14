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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('video', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='home/img/apps/thumbnails/')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Art',
                'verbose_name_plural': 'Art',
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('video', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='home/img/games/thumbnails/')),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(blank=True, to='home.Contributor')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(upload_to='home/img/libraries/thumbnails/')),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(blank=True, to='home.Contributor')),
            ],
            options={
                'verbose_name': 'Library',
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('video', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='home/img/tools/thumbnails/')),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(blank=True, to='home.Contributor')),
                ('links', models.ManyToManyField(blank=True, to='home.Link')),
            ],
            options={
                'verbose_name': 'Tool',
                'verbose_name_plural': 'Tools',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('posted', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tutorial',
                'verbose_name_plural': 'Tutorials',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('thumbnail', models.ImageField(upload_to='home/img/sites/thumbnails/')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
        ),
        migrations.AddField(
            model_name='library',
            name='links',
            field=models.ManyToManyField(blank=True, to='home.Link'),
        ),
        migrations.AddField(
            model_name='game',
            name='links',
            field=models.ManyToManyField(blank=True, to='home.Link'),
        ),
        migrations.AddField(
            model_name='app',
            name='contributors',
            field=models.ManyToManyField(blank=True, to='home.Contributor'),
        ),
        migrations.AddField(
            model_name='app',
            name='links',
            field=models.ManyToManyField(blank=True, to='home.Link'),
        ),
    ]
