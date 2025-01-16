'''
Caitlin Sheeran
01/10/2025
Function Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# function = A block of reusable code   place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()

happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
happy_birthday("Joe", 40)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Caitlin", 42.50, "01/02/2025")
display_invoice("Joe", 67.80, "02/06/2025")

# return = state used to end a function and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name("Caitlin", "Sheeran")

print(full_name)