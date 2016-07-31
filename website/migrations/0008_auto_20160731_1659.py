# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-31 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20160731_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.AddField(
            model_name='prices',
            name='category',
            field=models.IntegerField(choices=[(1, 'Dairy'), (2, 'Digestives'), (3, 'Drinks and Beverages'), (4, 'Food'), (5, 'Morning Misc'), (7, 'NUtrition'), (8, 'Snackes')], default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]