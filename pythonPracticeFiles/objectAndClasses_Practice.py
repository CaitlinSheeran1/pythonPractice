'''
Caitlin Sheeran
01/13/2025
Object and Class Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# Object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a class to create many objects


# class = (blueprint) used to design the structure and layout of an object


class Car:

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")



car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Fussion", 2016, "black", True)

print(car1.model)
car2.stop()
car1.describe()
