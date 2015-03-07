import time
import math

start = time.clock()

factorials = []
for digit in range(0, 10):
    factorials.append(math.factorial(digit))


number = 10
sum = 0
while number < 1000000:
    digitSum = 0
    numString = str(number)
    for digit in numString:
        d = int(digit)
        digitSum = digitSum + factorials[d]
    if digitSum == number:
        sum = sum + number
    number = number + 1
    
print sum

end = time.clock()
print end - start
