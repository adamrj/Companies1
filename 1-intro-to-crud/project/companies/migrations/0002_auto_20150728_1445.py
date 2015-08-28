# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, default=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
