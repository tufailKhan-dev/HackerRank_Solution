"""
using parent class method in our child class is called method overriding

"""

class Bank:
    def get_rate_of_interest(self):
        return 10
class SBI(Bank):
    def get_rate_of_interest(self):
        return 7
class ICICI(Bank):
    def get_rate_of_interest(self):
        return 8
b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank rate of Interest",b1.get_rate_of_interest())
print("SBI rate of interest",b2.get_rate_of_interest())
print("ICICI rate of interest",b3.get_rate_of_interest())

