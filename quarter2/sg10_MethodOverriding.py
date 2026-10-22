class Animal: # create a class called animal
    def __init__(self, name): # define the constructor method with a parameter name
        self.name = name # assign the value of the name parameter to the object's name attribute
    def eat(self): # define a method that is called eat to show when the animal eats
        print(f"{self.name} is eating.") # print a message stating that the animal is eating
    def make_sound(self): #define a method called make_sound
        print (f"{self.name} makes a sound.") #print a message stating that the animal makes a sound
        
class Lion(Animal): #create a child class called Lion that inherits from the Animal class (Parent class)
    def make_sound(self): #this is where u override the make_sound method specifically for lions
        print(f"{self.name} roars loudly!") #print a message stating that the lion is roaring loudly
    def eat(self): #ovverife eat method for lions
        print(f"{self.name} eats fresh meat.") #print message showing that the lion eats fresh meat

class Elephant(Animal): # create a child class called Elephant that inherits from the Animal class (the parent class)
    def make_sound(self): #override the make_sound method specically for elephants
        print(f"{self.name} trumpets!") # print message stating that elephent is trumpeting
    def eat(self): #override the eat method specifically for elephants
        print(f"{self.name} eats grass and fruits.") #print a message showing that the elephant eats grass and fruits

class Monkey(Animal): #make a child class called Monkey that inherits from the Animal class (the parent class)
    def make_sound(self): #override the make_sound method specifically for monkeys
        print(f"{self.name} chatters!") #print a message stating that the monkey chatters
    def eat(self): #override the eat method specifically for monkeys
        print(f"{self.name} eats bananas.") #print a message showing that the monkey eats bananas
    
animals = [ #create a list with instances of all the animal objects
    Lion("Simba"), # create the lion object with a name Simba and add it to the list
    Elephant("Dumbo"), #create an elephant object with a namw Dumbo and add it to the list
    Monkey("George")] #create a Monkey object named George and add it to the list

for animal in animals: #loop through every animal in the list (using for loop)
    animal.make_sound() #call the make_sound for the current animal
    animal.eat() #call eat for current animal
    print("------") # print dashes to separate the output/so it has a spacing between each animal
