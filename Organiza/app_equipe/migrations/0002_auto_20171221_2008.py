# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-21 22:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_equipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotores',
            name='promotores',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lideres',
            name='lideres',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jornada',
            name='dias_jornada',
            field=models.ManyToManyField(to='app_equipe.Dias'),
        ),
        migrations.AddField(
            model_name='jornada',
            name='jornada_equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_equipe.Equipe'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='lideres',
            field=models.ManyToManyField(to='app_equipe.Lideres'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='promotores',
            field=models.ManyToManyField(to='app_equipe.Promotores'),
        ),
    ]
