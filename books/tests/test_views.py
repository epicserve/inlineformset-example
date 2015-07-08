import unittest
from books.tests.base import BaseTest
from django.core.urlresolvers import reverse
from django.test import Client
from books.models import Book, Author

c = Client()


class TestCreateView(BaseTest):

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

        resp = c.get(self.url)
        self.assertEqual(resp.status_code, 200)

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


class TestUpdateView(BaseTest):

    def setUp(self):
        self.add_data()
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

        resp = c.get(self.url)
        self.assertEqual(resp.status_code, 200)

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


class TestBookListView(BaseTest):

    def test_view(self):
        self.add_data()
        resp = c.get(reverse('book_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['object_list']), 1)


class TestBookDetailView(BaseTest):

    def test_view(self):
        self.add_data()
        resp = c.get(reverse('book_detail', args=(self.book.pk,)))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['object'].title, self.book.title)


class TestAuthorList(BaseTest):

    def test_view(self):
        self.add_data()
        resp = c.get(reverse('author_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['object_list']), 1)


class TestAuthorDetail(BaseTest):

    def test_view(self):
        self.add_data()
        resp = c.get(reverse('author_detail', args=(self.author.pk,)))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['object'].name, self.author.name)
