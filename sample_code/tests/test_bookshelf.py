import unittest
from bookshelf import BookShelf, BookNotFound
from book import Book


class TestBookshelf(unittest.TestCase):

    def test_add_and_remove(self):
        shelf = BookShelf()
        for i in range(50):
            shelf.add(Book('Python Magic'))

        self.assertEqual(len(shelf.books), 50)

        shelf.remove('Python Magic')

        self.assertEqual(len(shelf.books), 49)

        with self.assertRaises(BookNotFound):
            shelf.remove('The Hidden Book')


if __name__ == '__main__':
    unittest.main()
