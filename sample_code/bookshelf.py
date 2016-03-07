class BookShelf(object):

    def __init__(self):
        self.rows = 6
        self.columns = 12
        self.books = []

    def add(self, book):
        self.books.append(book)

    def remove(self, title):
        try:
            idx = next(idx for idx, book in enumerate(self.books) if
                       book.title == title)
        except StopIteration:
            raise BookNotFound('Could not find book: %s' % title)

        del self.books[idx]

    def count(self):
        return len(self.books)

class BookNotFound(Exception):
    pass
