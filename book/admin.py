# encoding: utf-8

from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms

import requests
import json

from .models import Book

admin.site.unregister(Group)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        douban_id = cleaned_data.get('douban_id', False)

        if douban_id:
            douban_book_api = 'http://api.douban.com/v2/book/%d'
            douban_book = json.loads(requests.get(douban_book_api % douban_id).text)
            error_code = douban_book.get('code', False)
            if error_code != False:
                raise forms.ValidationError(u'不合法的豆瓣图书ID')
            else:
                return cleaned_data
        else:
            self.cleaned_data['douban_id'] = douban_id
            return cleaned_data


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('name', 'author', 'donor')
    fieldsets = (
        (u'基本信息', {
            'fields': ('douban_id', 'name', 'author', 'publisher', 'author_introduction',
                       'content_introduction', 'isbn')
        }),
        (None, {
            'fields': ('lib_index', 'donor', 'editor_comment')
        }),
    )
    search_fields = ('name', 'author')
