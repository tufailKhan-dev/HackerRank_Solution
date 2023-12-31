
#class - is a collection of objects
class car:
    # objects - is an entity that has state and behavior
    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)

if __name__ == "__main__":
    c1 = car("Toyota",2016)
    c1.display()

