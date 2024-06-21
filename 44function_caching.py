# Function Caching

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*n

print(fx(5))
print("5 done!!")
print(fx(10))
print("10 done!!")
print(fx(15))
print("15 done!!")

print("again\n")
print(fx(5))
print("5 done!!")
print(fx(10))
print("10 done!!")
print(fx(15))
print("15 done!!")
      
