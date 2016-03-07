from datetime import datetime
from json import JSONEncoder

from bookshelf import BookShelf
from person import Person


COMPLEX_OBJECTS = (BookShelf, Person)


class ObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return {'__type__': 'datetime.datetime',
                    'iso_format': obj.isoformat()}

        if isinstance(obj, COMPLEX_OBJECTS):
            obj_data = obj.__dict__.copy()
            obj_data['__type__'] = type(obj).__name__
            return obj_data

        if type(obj).__name__ == 'Book':
            obj_data = obj.__dict__.copy()
            obj_data['__type__'] = type(obj).__name__
            return obj_data

        super().default(obj)


def object_decoder(obj):

    if '__type__' in obj:
        cls_name = obj.pop('__type__')

        if cls_name == 'datetime.datetime':
            format_str = '%Y-%m-%dT%H:%M:%S.%f'
            return datetime.strptime(obj['iso_format'], format_str)

        elif cls_name == 'BookShelf':
            new_instance = BookShelf()
            new_instance.__dict__.update(obj)

            return new_instance

        elif cls_name == 'Book':
            module = __import__('book', globals(), locals(), [cls_name])
            klass = getattr(module, cls_name)
            book = klass(obj.pop('title'))
            book.__dict__.update(obj)

            return book

        elif cls_name == 'Person':
            new_instance = Person()
            new_instance.__dict__.update(obj)

            return new_instance

    return obj