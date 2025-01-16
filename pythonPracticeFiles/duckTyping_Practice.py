'''
Caitlin Sheeran
01/14/2025
Duck Typing Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# "Duck Typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minium necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck"


class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speal(self):
        print("Meow")

class Car:
    alive = False

    def speak(self):
        print("HONK")

animals = [Dog(), Cat(), Car()]


for animal in animals:
    animal.speak()
    print(animal.alive)