'''
Caitlin Sheeran
11/25/2024
Practice for collection types
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''
#Collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]

for x in fruits:
    print(x)
print("apple" in fruits)
print("pineapple" in fruits)

fruits.append("pineapple") #adds
fruits.remove("apple") #removes
fruits.insert("0, kiwi") #adds in certain index
fruits.sort() #sorts by letter
fruits.reverse() #stars at the end
fruits.clear() #gets rid of all of them
fruits.index("apple") # gets index
fruits.count("banana") # counts how many times its in list


sports = {"soccer", "baseball", "football", "basketball"}