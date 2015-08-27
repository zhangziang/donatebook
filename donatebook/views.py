# encoding: utf-8

from django.views.generic import TemplateView

from book.models import Book
from donor.models import Donor


class ListView(TemplateView):
    template_name = 'list.html'
    one_page_item = 10

    def get(self, request, page='1', *args, **kwargs):
        page = int(page)
        books = Book.objects.all().order_by('-id')
        book_num = len(books)
        before_page_num = (page-1)*self.one_page_item
        current_page_end = page*self.one_page_item

        button_type = 0

        if page-1 <= 0:
            before_page = False
        else:
            before_page = True
        if current_page_end >= book_num:
            after_page = False
        else:
            after_page = True

        if before_page_num >= book_num or before_page_num < 0:
            books = []
        elif current_page_end >= book_num:
            books = books[before_page_num:]
        else:
            books = books[before_page_num:current_page_end]

        # before_page = True
        # if before_page_num < 0:
        #     before_page = False
        #     after_page = False
        #     books = []
        # else:
        #     if before_page_num >= book_num:
        #         books = []
        #         after_page = False
        #     else:
        #         if current_page_end < book_num:
        #             books = books[before_page_num:current_page_end+1]
        #             after_page = True
        #         if current_page_end >= book_num:
        #             books = books[before_page_num:]
        #             after_page = False

        context = {
            'books': books,
            'before_page': before_page,
            'after_page': after_page,
            'button_type': button_type,
            'page_next': page+1,
            'page_last': page-1,

        }

        return  self.render_to_response(context)


class RankView(TemplateView):
    template_name = 'rank.html'

    def get_context_data(self, **kwargs):
        sql = "select donor_donor.id as id, donor_donor.name as name,college_college.name as collge, count(donor_donor.id) as cont from book_book, donor_donor,college_college where book_book.donor_id = donor_donor.id and donor_donor.college_id = college_college.id group by donor_donor.id  order by count(donor_donor.id) desc;"
        donate_rank = Book.objects.raw(sql)
        rank_new = []
        for rank, item in enumerate(donate_rank, 1):
            rank_one = {
                'rank': rank,
                'id': item.id,
                'name': item.name,
                'college': item.collge,
                'count': item.cont
            }
            rank_new.append(rank_one)

        kwargs['ranks'] = rank_new

        return super(RankView, self).get_context_data(**kwargs)

class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        search_key = request.GET.get("search_key", '')
        books = Book.objects.filter(name__contains=search_key)
        donors = Donor.objects.filter(name__contains=search_key)

        context = {
            'books': books,
            'donors': donors
        }

        return self.render_to_response(context)
