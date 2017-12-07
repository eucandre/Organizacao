# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-07 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('Segunda-feira', 'Segunda-feira'), ('Terca-feira', 'Terca-feira'), ('Quarta-feira', 'Quarta-feira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sabado', 'Sabado')], max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Dias da semana de jornada',
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Equipe',
            },
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('periodo', models.CharField(choices=[('Manha', 'Manha'), ('Tarde', 'Tarde'), ('Manha e Tarde', 'Manha_e_Tarde')], max_length=150)),
                ('de', models.TimeField()),
                ('ate', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Jornada de Trabalho',
            },
        ),
        migrations.CreateModel(
            name='Lideres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Lideres de Equipes',
            },
        ),
        migrations.CreateModel(
            name='Promotores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Promotores de vendas',
            },
        ),
    ]
