from django.conf.urls import url

from .views import DonorView

urlpatterns = [
    url(r'(?P<donor_id>[0-9]+)/$', DonorView.as_view(), name='one'),
]
