
#class ClassName:
class Person:
    #attributes ...
    def __init__(self):
        '''
        #this is the constructor method 
        that is called when creating a new Person object
        '''
        self.name = input("enter your name: ")
        self.age = input("enter your age: ")

    def greet(self):
        '''
            this is a method of the person class that prints a greeting message

        '''
        print("Hello, my name is " + self.name)

if __name__ == '__main__':
    person1 = Person()
    person1.greet()

