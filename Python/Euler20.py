import time
import math

start = time.clock()

number = 2
factorial = [1]
while number < 100:
    index = 0
    while index < len(factorial):
        factorial[index] = factorial[index] * number
        index = index + 1
    index = 0
    while index < len(factorial):
        if factorial[index] >= 10:
            if index == len(factorial) - 1:
                factorial.append(factorial[index] / 10)
            else:
                factorial[index + 1] = factorial[index + 1] + factorial[index] / 10
            factorial[index] = factorial[index] % 10
        index = index + 1
    number = number + 1

sum = 0
for digit in factorial:
    sum = sum + digit

print sum

end = time.clock()
print end - start
