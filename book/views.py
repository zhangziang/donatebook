# encoding: utf-8

from django.views.generic import TemplateView
from django.http.response import Http404

from .models import Book


class BookView(TemplateView):
    template_name = 'book.html'

    def get(self, request, book_id, *args, **kwargs):
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            book = None

        return self.render_to_response({'book': book})
