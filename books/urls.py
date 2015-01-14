from django.conf.urls import patterns, url
from books import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BookList.as_view(), name='book_list'),
    url(r'^(?P<pk>\d+)/$', views.BookDetail.as_view(), name='book_detail'),
    url(r'^add/$', views.AuthorCreateView.as_view(), name='add_author_and_books'),
    url(r'^(?P<pk>\d+)/edit/$', views.AuthorUpdateView.as_view(), name='edit_author_and_books'),
    url(r'^authors/$', views.AuthorList.as_view(), name='author_list'),
    url(r'^authors/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
)
