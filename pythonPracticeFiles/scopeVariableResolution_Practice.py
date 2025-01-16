'''
Caitlin Sheeran
01/13/2025
Variable Scope and Scope Resolution Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# Variable Scope: Where a variable is visible and accessible (functions can't see inside other functions)
# Scope Resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


from math import e

def func1():
    x = 1       # local version
    print(x)
    def func3():
        x = 3     #enclosed version
        print(x)

def func2():
    x = 2
    print(x)

def func4():
    print(e)   # built-in version

# x = 3      Global version

func1()
func2()
func4()