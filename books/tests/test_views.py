import unittest
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from books.models import Book, Author

c = Client()


class BaseTestCase(TestCase):

    def assertBasicRedirect(self, response, redirect_url):
        redirect_url = "http://testserver{}".format(redirect_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, redirect_url)


class TestCreateView(BaseTestCase):

    def setUp(self):
        self.url = reverse('add_author_and_books')

    @unittest.expectedFailure
    def test_empty_form(self):
        "The response returns a 403"
        c.post(self.url)

    def test_empty_form_with_manage_fields(self):
        resp = c.post(self.url, {
            'book_set-TOTAL_FORMS': 1,
            'book_set-INITIAL_FORMS': 0,
            'book_set-MIN_NUM_FORMS': 0,
            'book_set-MAX_NUM_FORMS': 1000,
        })
        self.assertEqual(resp.status_code, 200)
        # TODO: Fix it so the following test passes. Currently, the following test fails with the error,
        #       "AssertionError: The form 'form' in context 5 does not contain the field 'name'"
        #
        #       self.assertFormError(resp, 'form', 'name', 'This field is required.')
        #
        self.assertTrue('This field is required.' in resp.context['form'].errors['name'])
        self.assertFormsetError(resp, 'formset', 0, 'title', 'This field is required.')

    def test_form(self):
        resp = c.post(self.url, {
            'book_set-TOTAL_FORMS': 1,
            'book_set-INITIAL_FORMS': 0,
            'book_set-MIN_NUM_FORMS': 1,
            'book_set-MAX_NUM_FORMS': 1000,
            'name': 'Author',
            'book_set-0-title': 'Book 1'
        })

        author = Author.objects.first()
        book = Book.objects.first()
        self.assertBasicRedirect(resp, author.get_absolute_url())
        self.assertEqual(author.name, 'Author')
        self.assertEqual(book.title, 'Book 1')


class TestUpdateView(BaseTestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Author")
        self.book = Book.objects.create(author=self.author, title='Book 1')
        self.url = reverse('edit_author_and_books', args=(self.author.pk, ))

    @unittest.expectedFailure
    def test_empty_form(self):
        "The response returns a 403"
        c.post(self.url)

    def test_empty_form_with_manage_fields(self):
        resp = c.post(self.url, {
            'book_set-TOTAL_FORMS': 2,
            'book_set-INITIAL_FORMS': 1,
            'book_set-MIN_NUM_FORMS': 1,
            'book_set-MAX_NUM_FORMS': 1000,
            'book_set-0-id': self.book.pk,
        })
        self.assertEqual(resp.status_code, 200)
        # TODO: Fix it so the following test passes. Currently, the following test fails with the error,
        # "AssertionError: The form 'form' in context 5 does not contain the field 'name'"
        #
        #       self.assertFormError(resp, 'form', 'name', 'This field is required.')
        #
        self.assertTrue('This field is required.' in resp.context['form'].errors['name'])
        self.assertFormsetError(resp, 'formset', 0, 'title', 'This field is required.')

    def test_form(self):
        resp = c.post(self.url, {
            'book_set-TOTAL_FORMS': 1,
            'book_set-INITIAL_FORMS': 1,
            'book_set-MIN_NUM_FORMS': 0,
            'book_set-MAX_NUM_FORMS': 1000,
            'name': 'Author',
            'book_set-0-id': self.book.pk,
            'book_set-0-title': 'Book 1'
        })

        author = Author.objects.first()
        book = Book.objects.first()
        self.assertBasicRedirect(resp, author.get_absolute_url())
        self.assertEquals(Author.objects.count(), 1)
        self.assertEquals(Book.objects.count(), 1)
        self.assertEqual(author.name, 'Author')
        self.assertEqual(book.title, 'Book 1')
