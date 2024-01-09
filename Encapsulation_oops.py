
# encapsulation

class Student:
    #private variable
    # __nameOftheVariable
    __name = "this is private variable"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("this is private method")



obj = Student()

