# Docstrings (It is not ignored by compiler and It always write after function,class,etc.. definition and before body.)
def square(num):
    '''This function take a value and return square of number.'''
    print(num**2)

num = int(input("Enter a number:"))
square(num)
print(square.__doc__)