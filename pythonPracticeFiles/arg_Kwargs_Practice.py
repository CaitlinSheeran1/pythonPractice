'''
Caitlin Sheeran
01/11/2025
Args and kwargs Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#          * unpacking operator


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 6))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Peter", "Brown", "III")

print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street= "Happy St.", 
              city= "Detroit", 
              state="MI", 
              zip="54321",
              apt = "100")

print()


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Bill", "Brown",
               street="123 fake street",
               apt = "#100",
               city = "Detroit",
               state = "MI",
               zip = "54321")