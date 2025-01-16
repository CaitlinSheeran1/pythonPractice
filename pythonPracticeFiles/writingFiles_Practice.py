'''
Caitlin Sheeran
01/14/2025
Writing Files Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

employess = ["Bob", "Mark", "Joe", "Bill"]

txt_data = "I like pizza!"

file_path = "output.txt"

try:

    with open(file =file_path, mode= "a") as file:    # w - writes     a - appends
        file.write("\n" + txt_data)
        for employee in employess:
            file.write(employee + " ")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")