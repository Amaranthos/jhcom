# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default=models.CharField(max_length=50, unique=True), unique=True)),
                ('posted', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tutorial',
                'verbose_name_plural': 'Tutorials',
            },
        ),
        migrations.AlterField(
            model_name='app',
            name='contributors',
            field=models.ManyToManyField(blank=True, to='home.Contributor'),
        ),
        migrations.AlterField(
            model_name='app',
            name='links',
            field=models.ManyToManyField(blank=True, to='home.Link'),
        ),
        migrations.AlterField(
            model_name='game',
            name='contributors',
            field=models.ManyToManyField(blank=True, to='home.Contributor'),
        ),
        migrations.AlterField(
            model_name='game',
            name='links',
            field=models.ManyToManyField(blank=True, to='home.Link'),
        ),
        migrations.AlterField(
            model_name='library',
            name='contributors',
            field=models.ManyToManyField(blank=True, to='home.Contributor'),
        ),
        migrations.AlterField(
            model_name='library',
            name='links',
            field=models.ManyToManyField(blank=True, to='home.Link'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='contributors',
            field=models.ManyToManyField(blank=True, to='home.Contributor'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='links',
            field=models.ManyToManyField(blank=True, to='home.Link'),
        ),
    ]
