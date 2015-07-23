# encoding: utf-8

from django.views.generic import TemplateView

from .models import Donor
from book.models import Book


class DonorView(TemplateView):
    template_name = 'donor.html'

    def get(self, request, donor_id, *args, **kwargs):
        donor_books = {}

        try:
            donor = Donor.objects.get(pk=donor_id)
        except Donor.DoesNotExist:
            pass
        else:
            books = Book.objects.filter(donor=donor)
            donor_books['count'] = len(books)
            donor_books['college'] = donor.college.name
            donor_books['name'] = donor.name
            donor_books['books'] = books

        return self.render_to_response(context=donor_books)
