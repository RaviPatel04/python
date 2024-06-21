# 'is' vs '==' 

a = 3   # store a & b as same location becuase 3 is constant it can't change
b = 3
print(a is b) # Get exact location of object in memory
print(a == b) # check value is equal or not


print("\n")
c = [3, 13, 23]
d = [3, 13, 23]
print(c is d) # get false because list is mutable so store in differnt location
print(c == d)

print("\n")
e = (3, 23, 13) # tuple is immutable so store e & f as same location
f = (3, 23, 13)
print(e is f)
print(e == f)