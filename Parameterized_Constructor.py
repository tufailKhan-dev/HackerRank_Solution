"""
------Constructor--------
A constructor is a special type of method (function) which is used to initialize the instance of members of the class.

Constructor can be Two types.
1. Parameterized constructor
2. Non parametrized constructor

--------Parameterized constructor-----------

"""
class Employee:
    def __init__(self,name,Id):
        self.id = Id
        self.name = name

    def display(self):
        print(f"Id: {self.id}, Name:{self.name}")

emp1 = Employee("Tufail",21)

emp1.display()
