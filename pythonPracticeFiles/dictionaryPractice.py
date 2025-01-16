'''
Caitlin Sheeran
01/09/2025
Dictionary Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# dictionary = a collection of {key:value} paris ordered and changeable. No duplicates


capitals = {"USA": "Washington D.C",
            "India": "New Delhu",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) #Update a new key to dictionary
capitals.update({"USA": "Detroit"})  # Change value

capitals.pop("China") #remove a key

#  capital.clear()   clears the dictionary

#keys = capitals.keys()

print(capitals)

for key in capitals.keys():
    print(key)

#values = capitals.values()

for value in capitals.values():
    print(value)

#items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")