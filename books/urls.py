from django.conf.urls import patterns

urlpatterns = patterns('books.views',
    (r'^$', 'book_list', {}, 'book_list'),
    (r'^(?P<pk>\d+)/$', 'book_detail', {}, 'book_detail'),
    (r'^add/$', 'manage_books', {}, 'add_author_and_books'),
    (r'^(?P<pk>\d+)/edit/$', 'manage_books', {}, 'edit_author_and_books'),
    (r'^authors/$', 'author_list', {}, 'author_list'),
    (r'^authors/(?P<pk>\d+)/$', 'author_detail', {}, 'author_detail'),
)
