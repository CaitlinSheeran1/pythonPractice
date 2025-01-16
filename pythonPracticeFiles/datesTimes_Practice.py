'''
Caitlin Sheeran
01/15/2025
Dates and Times Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

import datetime

date = datetime.date(2025, 1, 14)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now_datetime = datetime.datetime.now()

#now_datetime = now_datetime.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)

if target_datetime < now_datetime:
    print("Target date has paseed")
else:
    print("Target date has NOT passed")



print(date)
print(today)
print(time)
print(now_datetime)