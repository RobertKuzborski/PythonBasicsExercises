
class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'My name is {self.name}')


person = Person('Rob')
person.talk()