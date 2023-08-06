# If Else Conditional Statements

# vote or not
age = int(input("\nEnter your age: "))

if(age <= 18):
    print("You can vote!!")
else:
    print("You can't vote!!")

# result
marks = int(input("\nEnter a marks between 1-70: "))

if(marks <= 30):
    print("Sorry!! you can try again!!")
elif(marks <=70):
    print("Congratulation!! you have cleared!!")
else:
    print("Enter a marks between 1-70!!")

# largest number from 3
a = int(input("\nEnter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if(a > b):
    if(b > c):
        print(a , " is large.")
    else:
        print(c , " is large.")
else:
    if(b > c):
        print(b , " is large.")
    else:
        print(c , " is large.")