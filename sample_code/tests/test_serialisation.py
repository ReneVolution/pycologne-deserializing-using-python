import json
import unittest
from ..bookshelf import BookShelf
from ..book import Book
from ..person import Person

from ..serializer import ObjectEncoder, object_decoder


class TestSerialisation(unittest.TestCase):

    def test_serializing_roundtrip(self):
        shelf = BookShelf()
        for i in range(42):
            shelf.add(Book('Python Magic'))

        with open('../bookshelf.json', 'w') as json_file:
            json.dump(shelf, json_file, cls=ObjectEncoder, indent=4)

        with open('../bookshelf.json', 'r') as json_file:
            shelf = json.load(json_file, object_hook=object_decoder)

        self.assertIsInstance(shelf, BookShelf)

        self.assertEqual(shelf.count(), 42)

        for book in shelf.books:
            self.assertIsInstance(book, Book)
            self.assertIsInstance(book.author, Person)


if __name__ == '__main__':
    unittest.main()
