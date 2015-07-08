from books.models import Author, Book
from django.test import TestCase


class BaseTest(TestCase):

    def add_data(self):
        self.author = Author.objects.create(name="C.S. Lewis")
        self.book = Book.objects.create(author=self.author, title='Mere Christianity')

    def assertBasicRedirect(self, response, redirect_url):
        redirect_url = "http://testserver{}".format(redirect_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, redirect_url)
