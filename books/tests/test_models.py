from books.tests.base import BaseTest


class TestAuthor(BaseTest):

    def test_str(self):
        self.add_data()
        self.assertEqual(unicode(self.author), self.author.name)


class TestBook(BaseTest):

    def test_str(self):
        self.add_data()
        self.assertEqual(unicode(self.book), self.book.title)
