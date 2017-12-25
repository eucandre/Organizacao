# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-25 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo_clientes',
            options={'verbose_name_plural': 'Grupo de Clientes atendidos'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='imagem_loja',
            field=models.ImageField(upload_to='documents/%Y/%m/%d'),
        ),
    ]