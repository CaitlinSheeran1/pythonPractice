'''
Caitlin Sheeran
01/11/2025
Iterables Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# Iterables = An object/collection that can return its
#             elements one at a time, allowing it to 
#             be iterated over in a loop


numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end = ' ')


print()

fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)

print()

name = "Caitlin Sheeran"

for character in name:
    print(character, end = " ")

print()

my_dictionary = {"A":1, "B": 2, "C": 3}

for value in my_dictionary.values():
    print(value)