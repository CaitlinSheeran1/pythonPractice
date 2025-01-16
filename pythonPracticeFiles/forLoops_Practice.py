'''
Caitlin Sheeran
11/25/2024
Practice for for loops
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''
#For loops: Execute a block of code a fixed number of times
#           You can iterate over a range, string, sequence, etc



for i in reversed(range(1, 11)):
    print(i)

print("HAPPY NEW YEAR")




credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)


    

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)