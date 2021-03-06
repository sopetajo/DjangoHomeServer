# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Probe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostName', models.CharField(max_length=100)),
                ('hostAdress', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='probe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pycanc.Probe'),
        ),
    ]
