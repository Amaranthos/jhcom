# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default=models.CharField(max_length=50, unique=True), unique=True)),
                ('video', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='home/img/apps/thumbnails/')),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Apps',
                'verbose_name': 'App',
            },
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Art',
                'verbose_name': 'Art',
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Contributors',
                'verbose_name': 'Contributor',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default=models.CharField(max_length=50, unique=True), unique=True)),
                ('video', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='home/img/games/thumbnails/')),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(to='home.Contributor', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Games',
                'verbose_name': 'Game',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default=models.CharField(max_length=50, unique=True), unique=True)),
                ('thumbnail', models.ImageField(upload_to='home/img/libraries/thumbnails/')),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(to='home.Contributor', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Libraries',
                'verbose_name': 'Library',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Links',
                'verbose_name': 'Link',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('thumbnail', models.ImageField(upload_to='home/img/sites/thumbnails/')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Sites',
                'verbose_name': 'Site',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default=models.CharField(max_length=50, unique=True), unique=True)),
                ('video', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='home/img/tools/thumbnails/')),
                ('description', models.TextField()),
                ('posted', models.DateField(auto_now_add=True)),
                ('contributors', models.ManyToManyField(to='home.Contributor', blank=True)),
                ('links', models.ManyToManyField(to='home.Link', blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'Tools',
                'verbose_name': 'Tool',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default=models.CharField(max_length=50, unique=True), unique=True)),
                ('posted', models.DateField(auto_now_add=True)),
                ('site', models.ForeignKey(to='home.Site')),
            ],
            options={
                'verbose_name_plural': 'Tutorials',
                'verbose_name': 'Tutorial',
            },
        ),
        migrations.AddField(
            model_name='library',
            name='links',
            field=models.ManyToManyField(to='home.Link', blank=True),
        ),
        migrations.AddField(
            model_name='library',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='game',
            name='links',
            field=models.ManyToManyField(to='home.Link', blank=True),
        ),
        migrations.AddField(
            model_name='game',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='app',
            name='contributors',
            field=models.ManyToManyField(to='home.Contributor', blank=True),
        ),
        migrations.AddField(
            model_name='app',
            name='links',
            field=models.ManyToManyField(to='home.Link', blank=True),
        ),
        migrations.AddField(
            model_name='app',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
        ),
    ]
