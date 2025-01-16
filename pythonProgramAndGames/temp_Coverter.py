'''
Caitlin Sheeran
11/24/2024
Pratice for making a temp coverter
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''



unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))


if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}" + chr(176) + "F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}"+ chr(176) + "C")
else:
    print(f"{unit} is an invalid unit of measurement")
