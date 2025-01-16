'''
Caitlin Sheeran
01/10/2025
Default Arguments Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more felexible, reduce # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. 

import time 


def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))

print(net_price(500, 0.1))



def count( end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)
count(30,15)