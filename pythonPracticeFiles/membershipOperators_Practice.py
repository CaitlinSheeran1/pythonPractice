'''
Caitlin Sheeran
01/11/2025
Membership Operators Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# Membership operators = used to test wether a value or variable is found in a sequence
#                      (string, list, tuple, set, or dictionary)
#                      1. in
#                      1. not in


word = "apple"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

print()

students = {"Sam", "Peter", "Bill"}

student = input("Enter the name of the student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

print()

grades = {"Sandy": "A", 
          "Squidward": "B", 
          "Spongebob": "C"}

student2 = input("Enter the name of the student: ")

if student2 in grades:
    print(f"{student2}'s grade is {grades[student2]}")
else:
    print(f"{student2} was not found")