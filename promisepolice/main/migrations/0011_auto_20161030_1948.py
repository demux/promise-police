# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 19:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
        ),
    ]