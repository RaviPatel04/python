# Multilevel Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

dog = GoldenRetriever("Max", "Golden")
dog.show_details()



# Hybrid inheritance

class parent():
    pass

class child1(parent):
    pass

class child2(parent):
    pass

class child3(child1, child2):
    pass


#herarchical inheritance
class baseclass():
    pass

class derived1(baseclass):
    pass

class derived2(baseclass):
    pass

class childderived1(derived1):
    pass

class childderived2(derived2):
    pass
