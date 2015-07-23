# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('douban_id', models.IntegerField(null=True, verbose_name='\u8c46\u74e3ID', blank=True)),
                ('name', models.TextField(null=True, verbose_name='\u56fe\u4e66\u540d\u79f0', blank=True)),
                ('publisher', models.TextField(null=True, verbose_name='\u51fa\u7248\u793e', blank=True)),
                ('content_introduction', models.TextField(null=True, verbose_name='\u5185\u5bb9\u7b80\u4ecb', blank=True)),
                ('author', models.TextField(null=True, verbose_name='\u4f5c\u8005', blank=True)),
                ('author_introduction', models.TextField(null=True, verbose_name='\u4f5c\u8005\u7b80\u4ecb', blank=True)),
                ('douban_rating', models.FloatField(null=True, verbose_name='\u8c46\u74e3\u8bc4\u5206', blank=True)),
                ('front_cover_image', models.URLField(null=True, blank=True)),
                ('isbn', models.CharField(max_length=20, null=True, blank=True)),
                ('lib_index', models.CharField(max_length=50, null=True, verbose_name='\u56fe\u4e66\u9986\u7d22\u4e66\u53f7', blank=True)),
                ('editor_comment', models.TextField(default='\u7f16\u8f91\u4ec0\u4e48\u90fd\u6ca1\u6709\u7559\u4e0b\u3002', verbose_name='\u7f16\u8f91\u63a8\u8350', blank=True)),
                ('donor', models.ForeignKey(verbose_name='\u6350\u4e66\u5b66\u751f', to='donor.Donor')),
            ],
            options={
                'verbose_name': '\u56fe\u4e66',
                'verbose_name_plural': '\u56fe\u4e66',
            },
        ),
    ]
