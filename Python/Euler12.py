import time
import math

start = time.clock()

naturalNumber = 1
triangleNumber = 1

while True:
    index = 1
    count = 0
    while index <= math.sqrt(triangleNumber):
        if triangleNumber % index == 0:
            count = count + 1
        index = index + 1
    if count > 250:
        break
    naturalNumber = naturalNumber + 1
    triangleNumber = triangleNumber + naturalNumber

print triangleNumber

end = time.clock()
print end - start
