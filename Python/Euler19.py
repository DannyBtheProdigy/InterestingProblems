import time

start = time.clock()

weekday = 2
month = 1
year = 1901
count = 0

while year < 2001:
    if (weekday == 0):
        count = count + 1
    if (month == 9) or (month == 4) or (month == 6) or (month == 11):
        weekday = (weekday + 30) % 7
    elif (month == 2):
        if (year % 4) != 0:
            weekday = (weekday + 28) % 7
        else:
            weekday = (weekday + 29) % 7
    else:
        weekday = (weekday + 31) % 7
    if (month == 12):
        year = year + 1
        month = 1
    else:
        month = month + 1
        

print count

end = time.clock()
print end - start
