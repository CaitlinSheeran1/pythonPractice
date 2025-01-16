'''
Caitlin Sheeran
01/13/2025
Class Variables Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data all objects created from that class


class Student:

    class_year = 2024           # class variables
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Charlie", 19)
student2 = Student("Bob", 25)
student3 = Student("Mark", 22)
student4 = Student("Jose", 17)


print(student1.name)
print(student1.class_year)

print(Student.num_students)

print(f"Mt graduating class of {Student.class_year} has {Student.num_students} students")


