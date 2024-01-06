

#---------lambda-----------
def return_sum(func,l):
    result = 0
    for i in l:
        if func(i):
            result = result + i
    return result

if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9]
    x = lambda x : x%2 == 0
    y = lambda x : x%2 != 0
    z = lambda x : x%3 == 0
    print(return_sum(x,l))
    print(return_sum(y,l))
    print(return_sum(z,l))


"""
Difference
1.Lambda has no return value
2. One line
3. Not used for code reusability
4. No name

"""

"""
why?
1. Along with higher order functions
"""

