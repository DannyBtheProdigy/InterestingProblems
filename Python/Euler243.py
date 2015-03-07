import time
import math

start = time.clock()

threshold = 4.0 / 10.0
#threshold = 15499.0 / 94744.0

constant = 0.577215664901532
exponentialPart = math.exp(constant)

d = 2
while True:
    logPart = math.log(math.log(d))
    divisor = logPart * exponentialPart
    euler = d / divisor
    if (d / (d - 1)) < threshold:
        break
    d = d + 1

print result

end = time.clock()
print end - start
