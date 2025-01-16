'''
Caitlin Sheeran
01/12/2025
List Comprehension Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''


doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squres = [z * z for z in range(1,11)]

print(doubles)
print(triples)
print(squres)



fruits = [fruit.upper() for fruit in ["apples", "orange", "banana", "coconut"]]

print(fruits)

numbers = [1, -2, 3, -4, 5, -6]

positve_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]

print(positve_nums)
print(negative_nums)

print()

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60 ]

print(passing_grades)