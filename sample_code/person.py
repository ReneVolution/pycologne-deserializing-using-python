class Person(object):

    def __init__(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.title = "Dead Manager"

    @property
    def name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)