'''
Caitlin Sheeran
01/14/2025
Reading Files Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

file_path = "test.txt"

try:

    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have permission to read that file")