import time
import math

start = time.clock()

number = 2
abundant_set = set()
while number < 28123:
    if ((number % 2) == 0) or ((number % 3) == 0):
        divisor_sum = 1
        possible_divisor = 2
        root = math.sqrt(number)
        while possible_divisor  <= root:
            if (number % possible_divisor) == 0:
                divisor_sum = divisor_sum + possible_divisor
                if possible_divisor != root:
                    divisor_sum = divisor_sum + (number / possible_divisor)
            if divisor_sum > number:
                break
            possible_divisor = possible_divisor + 1
        if divisor_sum > number:
            abundant_set.add(number)
    number = number + 1


sum_set = set()

for abundant_1 in abundant_set:
    for abundant_2 in abundant_set:
        if (abundant_1 + abundant_2) < 28123:
            sum_set.add(abundant_1 + abundant_2)


final_sum = 0

n = 1

while n < 28123:
    if n not in sum_set:
        final_sum = final_sum + n
    n = n + 1


print final_sum

end = time.clock()
print end - start
