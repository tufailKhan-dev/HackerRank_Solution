"""
multilevel inheritence is possible in python like other object-oriented languages. Multi-level inheritence is archived when a derived class inherits another derived class. there is no limit on the number of levels up to which, the multilevel inheritence is archived in python.

"""

class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
class puppy(Dog):
    def eat(self):
        print("Eating bread")
d = puppy()
d.bark()
d.speak()
d.eat()

