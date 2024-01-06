
# reduce function

import functools

L = [1,2,345,3,5,2222,212]

m = functools.reduce(lambda x,y : x if x>y else y, L)

print(m)
