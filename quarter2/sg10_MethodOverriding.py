class Animal: # create a class called animal
    def __init__(self, name): # define the constructor method with a parameter name
        self.name = name # assign the value of the name parameter to the name attribute
    def eat(self): # define a method that is called eat
        print(f"{self.name} is eating.") # this is to print the name of the animal a
    def make_sound(self):
        print (f"{self.name} makes a sound.")
        
class Lion(Animal): 
    def make_sound(self):
        print(f"{self.name} roars loudly!")
    def eat(self):
        print(f"{self.name} eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets!")
    def eat(self):
        print(f"{self.name} eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} chatters!")
    def eat(self):
        print(f"{self.name} eats bananas.")
    
lion =Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("------")

print(elephant.make_sound())
print(elephant.eat())
print("------")

print(monkey.make_sound())
print(monkey.eat())
print("------")
