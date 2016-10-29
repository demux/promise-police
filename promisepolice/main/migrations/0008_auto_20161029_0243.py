# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20161029_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='parties_accused',
            field=models.ManyToManyField(blank=True, related_name='accused_by_claims', to='main.Party', verbose_name='Ásakapir flokkar'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='persons_accused',
            field=models.ManyToManyField(blank=True, related_name='accused_by_claims', to='main.Person', verbose_name='Ásakaðir aðilar'),
        ),
    ]
