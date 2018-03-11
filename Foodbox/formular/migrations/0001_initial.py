# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-11 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name2', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=40)),
                ('age', models.CharField(max_length=2)),
                ('gender', models.CharField(max_length=10)),
                ('current_weight', models.CharField(max_length=5)),
                ('desired_weight', models.CharField(max_length=5)),
                ('height', models.CharField(max_length=5)),
                ('duration', models.CharField(max_length=5)),
                ('restrictions', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
