# Decorators

def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello friends!!")
        fx(*args, **kwargs)
        print("Thanks for using this code!!\n")
    return mfx
    
@greet
def hello():
    print("Hello world!!")

hello()

@greet
def sum(a, b):
    print(a + b)

sum(13, 23)