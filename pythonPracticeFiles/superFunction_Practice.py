'''
Caitlin Sheeran
01/13/2025
Super() Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# super() = Function used in a child class to call methods from a parent class (supperclass)
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.4 * self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm^2")

    

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")


    
    
    


circle = Circle(color="red", is_filled = True, radius = 5)

square = Square(color="blue", is_filled = False, width = 6)

triangle = Triangle(color="green", is_filled = True, width = 7, height= 8)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

triangle.describe()
circle.describe()
square.describe()