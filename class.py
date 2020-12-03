class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. Hello!!'.format(self.name))

    def __del__(self):
        print('finished!')

person = Person('Donald')
person.say_something()

del person

print('last row of code')

