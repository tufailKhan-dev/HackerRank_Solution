
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Person1(Person):
    def intro(self):
        print(f"Hi my name is {self.name} and i am {self.age}")

if __name__ == "__main__":
    p1 = Person1("Tufail",21)
    p1.intro()


