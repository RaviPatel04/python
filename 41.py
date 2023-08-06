# Time Module 

import time

def usingfor():
    for i in range(10000):
        print(i)

def usingwhile():
    i = 0
    while(i < 10001):
        print(i)
        i = i + 1


r = time.time()
usingfor()
t1 = time.time() - r

r = time.time()
usingwhile()
t2 = time.time() - r



print(t1)
print(t2)


# sleep
print(4)
time.sleep(4)
print("hello!!")