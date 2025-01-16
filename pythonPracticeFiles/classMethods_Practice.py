'''
Caitlin Sheeran
01/14/2025
Class methods Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''


# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself


class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa


    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"

    

student1 = Student("Brain", 3.2)
student1 = Student("Mark", 2.0)
student1 = Student("Sandra", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())

    