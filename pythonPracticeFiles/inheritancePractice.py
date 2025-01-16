'''
Caitlin Sheeran
01/13/2025
Inheritance Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# Inheritance = Allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("Mark")
cat = Cat("Gilbert")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
mouse.sleep()