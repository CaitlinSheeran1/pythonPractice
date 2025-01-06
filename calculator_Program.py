'''
Caitlin Sheeran
11/24/2024
Pratice for making a caculator
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''


operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))


if operator =='+':
    result = num1 + num2
    print(round(result, 3))
elif operator =='-':
    result = num1 - num2
    print(round(result, 3))
elif operator =='*':
    result = num1 * num2
    print(round(result, 3))
elif operator =='/':
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")

