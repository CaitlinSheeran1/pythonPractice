'''
Caitlin Sheeran
01/06/2025
Shopping Cart Program
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q" :
        break
    else:
        price = float(input(f'Enter the price of a {food}: $'))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")