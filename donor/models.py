# encoding: utf-8

from django.db import models

from college.models import College


class Donor(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'捐书人')
    college = models.ForeignKey(to=College, verbose_name=u'所属学院')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'捐书人'
        verbose_name_plural = u'捐书人'
