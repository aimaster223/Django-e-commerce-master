# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-11 21:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address2',
            new_name='address_line2',
        ),
    ]
