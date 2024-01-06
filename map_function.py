
# map function

# map( func, *iterables) -> map object
l = [1,2,3,4,5,6,7]
m = map(lambda x : x*2, l)
# it returns map object
# to see map objects
# convert into list
b = list(m)
print(b)
