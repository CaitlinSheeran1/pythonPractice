'''
Caitlin Sheeran
11/25/2024
Practice for nested loops
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''
# to add varation to print, you can use end="" then you can add something in it

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of colums: "))
symbol = input('Enter a symbol to use')

for x in range(rows):
    for y in range(columns):
        print(symbol, end='')
    print()