# encoding: utf-8

from django.db import models

import json

import requests

from donor.models import Donor

from .utils import is_empty

class Book(models.Model):
    douban_id = models.IntegerField(verbose_name=u'豆瓣ID', null=True, blank=True)

    # according to douban_id get below data
    name = models.TextField(verbose_name=u'图书名称', null=True, blank=True)
    publisher = models.TextField(verbose_name=u'出版社', null=True, blank=True)
    content_introduction = models.TextField(verbose_name=u'内容简介', null=True, blank=True)
    author = models.TextField(verbose_name=u'作者', null=True, blank=True)
    author_introduction = models.TextField(verbose_name=u'作者简介', null=True, blank=True)
    douban_rating = models.FloatField(verbose_name=u'豆瓣评分', null=True, blank=True)
    front_cover_image = models.URLField(null=True, blank=True)

    isbn = models.CharField(max_length=20, null=True, blank=True)

    lib_index = models.CharField(verbose_name=u'图书馆索书号', max_length=50, null=True, blank=True)

    donor = models.ForeignKey(to=Donor, verbose_name=u'捐书人')
    editor_comment = models.TextField(verbose_name=u'编辑推荐', blank=True, default=u'编辑什么都没有留下。')

    def save(self, *args):
        douban_book_api = 'http://api.douban.com/v2/book/%d'
        if self.douban_id:
            douban_id = self.douban_id
            douban_book = json.loads(requests.get(douban_book_api % douban_id).text)

            if is_empty(self.name):
                self.name = douban_book.get('title', '')
            if is_empty(self.publisher):
                self.publisher = douban_book.get('publisher', '')
            if is_empty(self.content_introduction):
                self.content_introduction = douban_book.get('summary', '')
            if is_empty(self.author):
                self.author = ', '.join(douban_book.get('author', []))
            if is_empty(self.author_introduction):
                self.author_introduction = douban_book.get('author_intro', '')
            self.douban_rating = float(douban_book.get('rating', {}).get('average', ''))
            if is_empty(self.front_cover_image):
                self.front_cover_image = douban_book.get('images', {}).get('large', '')
            if is_empty(self.isbn):
                self.isbn = douban_book.get('isbn13', '')

        super(Book, self).save(*args)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'图书'
        verbose_name_plural = u'图书'
