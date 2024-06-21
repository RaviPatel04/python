# Tuples 

tuple0 = (3,13,23,33,43)
print(tuple0)
print(tuple0[1])
print(tuple0[-3])
print(tuple0[4])

tuple2 = tuple0[1:3]
print(tuple2)

# Operations on Tuples 

tuple1 = (3,13,23,33,43,53,3,3,3)
print(tuple1.count(3))
print(tuple1.index(23))
print(tuple1)

temp = list(tuple1)
temp.append("Hello!!")
temp.pop(3) #pop(delete) element from third index
temp[6] = 63 #add emlement 63 in 6th index
tuple1 = tuple(temp)
print(tuple1)
