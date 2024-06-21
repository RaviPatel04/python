# Recursion(function call itself)

# factorial find
num = int(input("Enter a number:"))
def factorial(num):
    if (num != 0):
        return num * factorial(num-1)
    else:
        return 1

print(factorial(num))

# fibonacci series
def fibonacci():
    pass