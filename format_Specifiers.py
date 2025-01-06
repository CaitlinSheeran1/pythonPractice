'''
Caitlin Sheeran
11/24/2024
Pratice for format specifiers
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''
#format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to the many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate postive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1 = 3000.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.2f}") # displays only 2 decimals
print(f"Price 2 is {price2:10}") # displays 10 characters
print(f"Price 3 is {price3:<10}") #starts at the left then goes 10 digits

print(f"Price 1 is {price1:<10}") # starts at the right then goes 10 digits
print(f"Price 2 is {price2:^10}") # centers the letter within the 10 digits
print(f"Price 3 is {price3:+}") # displays a + if number is postive 

print(f"Price 1 is {price1:,}") # adds a comma every 1000 place
print(f"Price 2 is {price2:+,.2f}") # you can combine them