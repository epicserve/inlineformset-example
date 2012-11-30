from django.conf.urls import patterns

urlpatterns = patterns('books.views',
    (r'^manage-books/$', 'manage_books', {'author_id': 1}, 'manage_books'),
)
