# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161028_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='the_truth',
            field=models.TextField(blank=True, verbose_name='Sannleikurinn'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='parties_accused',
            field=models.ManyToManyField(related_name='accused_by_claims', to='main.Party', verbose_name='Ásakapir flokkar'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='persons_accused',
            field=models.ManyToManyField(related_name='accused_by_claims', to='main.Person', verbose_name='Ásakaðir aðilar'),
        ),
    ]