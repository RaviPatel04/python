import random

char = "~!@#$%^&*({[_+-=|\\)}]?/><qwertyuiop12345asdfghjkl56789zxcvbnm0"
password=""

length = int(input("Entera a length of password : "))

if(length<8):
    print("Password must contain 8 letter!!")
else:
    for i in range(length):
        password+=random.choice(char)

print(password)

