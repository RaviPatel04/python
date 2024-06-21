# Multiple Inheritance

class namer:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(F"The name is {self.name}")

class dancer:

    def __init__(self, dance):
        self.dance = dance
    
    def show(self):
        print(f"The dance is {self.dance}")

        
class namerdancer(namer, dancer):

    def __init__(self, name, dance):
        self.name = name
        self.dance = dance
    
    
    

nd = namerdancer("Aayushi", "Garba") 
print(nd.name)
print(nd.dance)
nd.show()