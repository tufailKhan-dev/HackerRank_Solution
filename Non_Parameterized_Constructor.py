"""
----------Non_Parameterized constructor-----------
The non parameterized constructor uses when we do not want to manipulate the value or yhe constructor that has only self as an argument.Consider the following example.

"""

class Student:
    #Constructor-non parameterized
    def __init__(self):
        print("This is non parameterized constructor")
    def show(self,name):
        print("Hello",name)

student = Student()
student.show("john")

