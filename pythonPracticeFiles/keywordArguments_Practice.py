'''
Caitlin Sheeran
01/11/2025
Keyword Arguments Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# keyword arguments = an argument preceded by an identifier
#                     helps with readability order of
#                     arguments doesn't matter


def hello(gretting, title, first, last):
    print(f"{gretting} {title}{first} {last}")


hello("Hello", title="Mr.", last="Brown", first="Kevin")

for x in range(1,11):
    print(x, end= " ")

print()
print("1", "2", "3", "4", "5", sep='-')

def getPhone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = getPhone(country=1, area=123, first=456, last=7890)

print(phone_num)