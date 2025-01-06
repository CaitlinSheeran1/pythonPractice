'''
Caitlin Sheeran
11/25/2024
Creating a countdown timer
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

import time


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # adds another zero for counting ex 7 -> 07
    time.sleep(1) # Makes loop wait 1 second


print("TIME'S UP")