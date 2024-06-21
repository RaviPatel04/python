# Introduction to Lists

list = [13, 23, "python", 13.23, "hello"]
print(list)
print(list[1])
print(list[3])
print(list[4])
print(list[-5])

list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

# List Methods
l = [1,0,4,23,13,55,44,100]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.append(1323)
print(l)
print(l.index(4))
print(l.count(13))
m = [13,23]
l.extend(m)
print(l)