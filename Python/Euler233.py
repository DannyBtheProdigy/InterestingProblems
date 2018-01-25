import time
import math

start = time.clock()

n = 105
end = math.pow(10, 11)
count = 0
while n <= end:
    r2 = 2 * ((n / 2.0) * (n / 2.0))
    angle = 360.0 / 420.0
    n = n + 105    

print count

end = time.clock()
print end - start
