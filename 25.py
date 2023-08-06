# Map, Filter and Reduce


#-----Map-------
l = [0, 3, 13, 23, 33, 43]
# def cube(x):
#     return x*x*x

# print(list(map(cube, l))) # using function

print(list(map(lambda x:x*x*x , l))) # using lamda function

#------Filter------
def filter_func(l):
    return l > 3

print(list(filter(filter_func , l)))

#------Reduce------
from functools import reduce
print(reduce(lambda x, y: x + y, l))