'''
Caitlin Sheeran
01/14/2025
Static Mehods Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''


# Static Methods = A method that belong to a class rather than any object from that class (instance)
#                  Usally used for general utility functions


# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utlity functions that do not access to class data

class Employee:

    def __init__(self, name, position):  # Instance
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod                       # Static
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]

        return position in valid_positions

employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Spongebob", "Cook")
employee3 = Employee("Squidward", "Cashier")


print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Rocket Scientist"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())