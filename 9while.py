# While Loops

i = 1
while (i <= 10):
    print(i)
    i = i + 1
else:
    print("incremented While loop is terminated!!")

j = 10
while(j > 0):
    print(j)
    j = j - 1
else:
    print("decreamented While loop is terminated!!")


b=0
x=0
while b<=10: #nested while
    print ('here is the outer loop\n',b)
    while x<=15:
        print('here is the inner loop\n',x)
        x=x+1
    b=b+1