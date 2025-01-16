'''
Caitlin Sheeran
01/14/2025
File Detection Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

import os

file_path = "test.txt"
# file_path = "folder/test.txt"      if the file is in another folder
# file_path = "C:\\Users\\HP\\Desktop\\test.txt"      

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):  # a folder
        print("That is a directory")

else:
    print("That location doesn't exist")