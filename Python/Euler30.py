import time
import math

start = time.clock()

number = 100

result_set = set()

while number < 1000000:
    digit1 = number % 10
    digit2 = (number / 10) % 10
    digit3 = (number / 100) % 10
    digit4 = (number / 1000) % 10
    digit5 = (number / 10000) % 10
    digit6 = number / 100000

    power_sum = pow(digit1, 5) + pow(digit2, 5) + pow(digit3, 5) + pow(digit4, 5) + pow(digit5, 5) + pow(digit6, 5)
    if(power_sum == number):
        result_set.add(number)
    
    number = number + 1

print(sum(result_set))

end = time.clock()
print end - start
