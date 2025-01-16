'''
Caitlin Sheeran
01/06/2025
2d List Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
'''
groceries = [["apple", "orange", "banana", "coconut",
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

This also works
'''

print(groceries[0])  #prints the whole first list instead of the first item

print(groceries[0][0]) #prints apple since it is in the first line and the first item

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()