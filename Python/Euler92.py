import time
import math

start = time.clock()

startingNumber = 9999999
set89 = set()
set89.add(89)
set1 = set()
set1.add(1)

set89_bounded = set()
set89_bounded.add(89)

while startingNumber > 1:
    current_set = []
    current_set.append(startingNumber)
    current_number = startingNumber
    while((current_number not in set89) and (current_number not in set1)):
        current_set.append(current_number)
        number_string = repr(current_number)
        current_length = len(number_string)
        index = 0
        next_number = 0
        while index < current_length:
            next_number = next_number + pow(int(number_string[index]), 2)
            index = index + 1

        current_number = next_number

    if(current_number in set89):
        for number in current_set:
            set89.add(number)
            if(current_number < 10000000):
                set89_bounded.add(number)
        
    else:
        for number in current_set:
            set1.add(number)

    startingNumber = startingNumber - 1

print(len(set89_bounded))

end = time.clock()
print end - start
