# For Loops

name = 'ravi'
for i in name:
    print(i)

print("\nfor in list")
colors = ['red','green','black','white']
for color in colors:
    print(color)
    for j in color:
        print(j)

print("\nusing range")
for r in range(13):
    print(r)

# for Loop with else
for l in range(6):
    print(l)            #if we use break in for loop then else doesn't executed.
else:
    print("loop successfully executed!!")