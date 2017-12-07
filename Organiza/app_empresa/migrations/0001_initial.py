# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-07 02:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dados_na_Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=150)),
                ('data_adminissao', models.DateField()),
                ('tipo_remuneracao', models.CharField(choices=[('Horista', 'horista'), ('Mensalista', 'Mensalista')], max_length=150)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Dados do Colaborador na Empresa',
            },
        ),
    ]
