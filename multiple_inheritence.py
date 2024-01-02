"""
Python provides us the flexibility to inherit multiple base classes in the child
class.
"""
#base class
class calculation1:
    def summation(self,a,b):
        return a+b

#base class
class calculation2:
    def multiplication(self,a,b):
        return a*b
#derived class
class Derived(calculation1,calculation2):
    def Divide(self,a,b):
        return a/b
d = Derived()
print(d.summation(1,1))
print(d.multiplication(10,1))
print(d.Divide(10,2))

