import time

start = time.clock()

sum = 0
sumSquares = 0
number = 1

while number < 101:
    sum = sum + number
    sumSquares = sumSquares + number * number
    number = number + 1

squaredSum = sum * sum
difference = squaredSum - sumSquares

print difference

end = time.clock()
print end - start
