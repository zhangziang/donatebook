# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='donor',
            field=models.ForeignKey(verbose_name='\u6350\u4e66\u4eba', to='donor.Donor'),
        ),
    ]
