# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 07:25
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170122_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
