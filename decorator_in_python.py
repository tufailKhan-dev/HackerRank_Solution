
#--------Decorators---------------

"""
decorators is used to modify function

"""

def greet(fx):
    def mfx():
        print("good")
        fx()
        print("thnaks for using this")
    return mfx
@greet
def hello():
    print("hi")
if __name__ == "__main__":
    hello()
