Name: Stacey Fame N. Nacion
Section: 9 - Platinum

Instruction: Do what is asked in each item below:

1. Answer the following questions:

a. What is duck typing, as explained in the video?
- Based on the video I have watched, it explains that duck typing is basically another way to achieve polymorphism in python without needing inheritance. So, instead of checking what class an object belongs to, Python  only checks if the object has the needed method or attribute. The video also stated the idea that "if it looks like a duck and quacks like a duck, then it must be a duck." 
- This isn't based on the video, but when i have searched more about duck typing, it states that duck typing enables polymorphism, where you can use objects of different types interchangeably, provided that they implement certain behaviors. An essential of this type (duck typing) of polymorphism is that the objects don't have to inherit from a common superclass, which makes code less rrigid and more adaptable to change.

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
- In the video, the Car class needed to have the speak() method which is the same method name used by the Dog and Cat, and the alive attribute so that it could run in the same loop without an error occuring.

2. Create the Python code that:

a. Creates three classes: Car, Boat, and Drone with a method move().
    move() in the Car class prints "The car drives on the road."
    move() in the Boat class prints "The boat sails on water."
    move() in the Drone class prints "The drone flies in the sky."

b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().

c. Creates one object of each class.

d. Calls the start_trip() method for each object.

Code: 

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car=Car()
boat=Boat()
drone=Drone()
start_trip(car)
start_trip(boat)
start_trip(drone)


3. How does the code in 2.2 demonstrate polymorphism?
- The code in 2.2 demonstrate polymorphism because rhe start_trip() function uses the same vehicle.move() method call for three different classes(Car, Boat, and Drone) that aren't connected by inheritance. Even though we call the exact same method (move()), each object does its own specific action and also prints a different output.



References:
- Bro Code. (2024, June 25). Learn python duck typing in 4 minutes! 🦆 [Video]. YouTube. https://www.youtube.com/watch?v=Qe03kCuTMoU
- Ramos, L. P. (2024, February 26). Duck typing in python: Writing flexible and decoupled code. Real Python. Realpython.Com. https://realpython.com/duck-typing-python/
