"""donatebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from .views import ListView, RankView, SearchView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/(?P<page>[0-9]+)/$', ListView.as_view()),
    url(r'^list$', ListView.as_view(), name='list'),
    url(r'^book/', include('book.urls', namespace='book')),
    url(r'^rank/$', RankView.as_view(), name='rank'),
    url(r'^donor/', include('donor.urls', namespace='donor')),
    url(r'^search/', SearchView.as_view(), name='search')
]
