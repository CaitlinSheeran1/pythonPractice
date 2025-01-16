'''
Caitlin Sheeran
01/14/2025
Exception Handling Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# exception = An event that iterrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))

    print(1 / number)
except ZeroDivisionError:
    print("You can not divide by")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")