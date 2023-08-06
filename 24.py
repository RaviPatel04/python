# Lambda functions

square = lambda x: x*x
print(square(12))

average = lambda x, y: (x + y)/2
print(average(13, 5))

def threesum(sum , x, y):
    return 7 + sum(x, y)

print(threesum(lambda x, y: (x + y), 3, 2))