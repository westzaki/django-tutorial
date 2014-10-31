from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^v1/books/$', views.book_list, name='book_list'),
)