'''
Caitlin Sheeran
11/24/2024
Weight coverter
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''


weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K or L): ")


if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = 'Kgs.'
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f'{unit} was not valid')
