# Inheritance

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  # in brackets it is the class inherits from
    pass  # pass statement is because class cant be empty, does nothing


class Cat(Mammal):
    def maw(self):
        print("weoww")


dog1 = Dog()
dog1.walk()  # wothout parenteces doesnt execute :O

