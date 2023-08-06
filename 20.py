# Raising custom errors

num = int(input("Enter a number positive number only:"))

if(num < 0):
    raise ValueError("You entered number should be negative!!")

print("Thank you!!")

# # Short hand if else
# a = 12
# b = 13

# print("a>b") if a>b else print("b>a") 