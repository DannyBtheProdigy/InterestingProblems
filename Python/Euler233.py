import time
import math

start = time.clock()

n = 105

sum = 0
while n < 100000000000:
    x = 0
    integerCoordinates = 0
    while x < n:
        if integerCoordinates > 105:
            break
        y = math.sqrt(math.pow(n, 2) - math.pow(x, 2))
        if math.floor(y) == y:
            integerCoordinates = integerCoordinates + 1
        x = x + 1
    if integerCoordinates == 105:
        sum = sum + n
    n = n + 1

print integerCoordinates * 4    

end = time.clock()
print end - start
