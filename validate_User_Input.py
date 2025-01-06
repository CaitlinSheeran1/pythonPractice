'''
Caitlin Sheeran
11/24/2024
Pratice for validate inputs with restrictions
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

username = input('Enter a username: ')

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")