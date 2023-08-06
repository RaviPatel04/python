# Operator Overloading 

class vector():
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self ,x):
        return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k "
    

v1 = vector(3, 13, 23)
print(v1)

v2 = vector(23, 13, 3)
print(v2)

print(v1 + v2)