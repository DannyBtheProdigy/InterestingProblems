import time
import math

start = time.clock()

diagonal_sum = 1
adder = 2
val = 1
corner_index = 0

while(adder < 1001):
    while(corner_index < 4):
        val = val + adder
        diagonal_sum = diagonal_sum + val
        corner_index = corner_index + 1
    adder = adder + 2
    corner_index = 0

print(diagonal_sum)

end = time.clock()
print end - start
