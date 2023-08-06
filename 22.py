# Local vs Global Variables

x = 3
print(x)
def hello():
    x = 13
    y = 23
    print(f"Local variable x is {x}")
    print(f"Local variable y is {y}")

hello()

print(f"Global variable x is {x}")
# print(f"Local variable y is {y}")  #Get error because y is local variable so it can't access outside funcion


print("\nChanged global variable inside a function")
a = 23
print(f"outside the function a is {a}")

def hello1():
    global a
    a = 13
    print(f"a changed globally inside a function: {a}")

hello1()
print(f"After a function a is: {a}")
    