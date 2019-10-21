# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-03 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170703_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewWriting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Genre')),
            ],
        ),
    ]