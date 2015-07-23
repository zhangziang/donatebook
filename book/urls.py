from django.conf.urls import url

from .views import BookView

urlpatterns = [
    url(r'^(?P<book_id>[0-9]+)/$', BookView.as_view(), name='one'),
]
