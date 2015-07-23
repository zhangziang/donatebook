# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u6350\u4e66\u4eba')),
                ('college', models.ForeignKey(verbose_name='\u6240\u5c5e\u5b66\u9662', to='college.College')),
            ],
            options={
                'verbose_name': '\u6350\u4e66\u4eba',
                'verbose_name_plural': '\u6350\u4e66\u4eba',
            },
        ),
    ]
