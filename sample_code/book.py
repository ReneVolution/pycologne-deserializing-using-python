from datetime import datetime
from person import Person


class Book(object):

    def __init__(self, title):
        self.created_at = datetime.now()
        self.title = title
        self.author = Person()
        self.description = 'No Description available'
