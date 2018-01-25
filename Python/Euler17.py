import time
import math

start = time.clock()

number = 1
count = 0
while number <= 1000:
    if (number / 1000) == 1:
        count = count + len("one")
        count = count + len("thousand")
    else:
        if ((number / 100) != 0) and ((number / 1000) == 0):
            count = count + len("hundred")
            if (number % 100) != 0:
                count = count + len("and")
            if (number / 100) == 1:
                count = count + len("one")
            if (number / 100) == 2:
                count = count + len("two")
            if (number / 100) == 3:
                count = count + len("three")
            if (number / 100) == 4:
                count = count + len("four")
            if (number / 100) == 5:
                count = count + len("five")
            if (number / 100) == 6:
                count = count + len("six")
            if (number / 100) == 7:
                count = count + len("seven")
            if (number / 100) == 8:
                count = count + len("eight")
            if (number / 100) == 9:
                count = count + len("nine")        
        if ((number / 10) % 10) == 1:
            if (number % 10) == 0:
                count = count + len("ten")
            if (number % 10) == 1:
                count = count + len("eleven")
            if (number % 10) == 2:
                count = count + len("twelve")
            if (number % 10) == 3:
                count = count + len("thirteen")
            if (number % 10) == 4:
                count = count + len("fourteen")
            if (number % 10) == 5:
                count = count + len("fifteen")
            if (number % 10) == 6:
                count = count + len("sixteen")
            if (number % 10) == 7:
                count = count + len("seventeen")
            if (number % 10) == 8:
                count = count + len("eighteen")
            if (number % 10) == 9:
                count = count + len("nineteen")
        else:
            if ((number / 10) % 10) == 2:
                count = count + len("twenty")
            if ((number / 10) % 10) == 3:
                count = count + len("thirty")
            if ((number / 10) % 10) == 4:
                count = count + len("forty")
            if ((number / 10) % 10) == 5:
                count = count + len("fifty")
            if ((number / 10) % 10) == 6:
                count = count + len("sixty")
            if ((number / 10) % 10) == 7:
                count = count + len("seventy")
            if ((number / 10) % 10) == 8:
                count = count + len("eighty")
            if ((number / 10) % 10) == 9:
                count = count + len("ninety")
            if (number % 10) == 1:
                count = count + len("one")
            if (number % 10) == 2:
                count = count + len("two")
            if (number % 10) == 3:
                count = count + len("three")
            if (number % 10) == 4:
                count = count + len("four")
            if (number % 10) == 5:
                count = count + len("five")
            if (number % 10) == 6:
                count = count + len("six")
            if (number % 10) == 7:
                count = count + len("seven")
            if (number % 10) == 8:
                count = count + len("eight")
            if (number % 10) == 9:
                count = count + len("nine")
        
    number = number + 1

print count
            
end = time.clock()
print end - start
