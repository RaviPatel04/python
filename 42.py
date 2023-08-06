# Walrus Operator  :=

a = True
# print (a = False) # get error becuse we alredy assinged a is true so this is sloved by using walrus operator

print( a:= False)

numbers = list()
while(number := int(input("Enter a number:"))) != 12: 
    numbers.append(number)
    print(numbers)


print("Your added numbers:",numbers)