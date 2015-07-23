# encoding: utf-8

from django.db import models


class College(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'学院名称')
    info = models.TextField(verbose_name=u'学院介绍', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'学院'
        verbose_name_plural = u'学院'
