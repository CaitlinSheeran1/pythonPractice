'''
Caitlin Sheeran
01/12/2025
Match-case Statement Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

# Match-case statement (switch): An alternative to using many elif
#                                statements. Execute code if a value
#                                matches a 'case' 
#                                Benefits: cleaner and syntax is more readable


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:                        # the underscore acts as a else
            return "Not a valid day"



def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":   # | acts as an or
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:                       # the underscore acts as a else
            return "Not a valid day"

print(day_of_week(2))

print(is_weekend("Sunday"))