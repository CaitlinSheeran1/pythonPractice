'''
Caitlin Sheeran
01/09/2025
Random Number Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

import random

# number = random.randint(1, 6)                              # Set numbers to be in range
# print(number)




# low = 1
# high = 100
# number2 = random.ranint(low, high)                         # Set variables to be a ligh or low number
# print(number2)


# number = random.random()                                   # picks a random floating number between 0-1

options  = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

option = random.choice(options)

print(option)

random.shuffle(cards)

print(cards)