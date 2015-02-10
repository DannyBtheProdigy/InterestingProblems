import time

start = time.clock()

digits = [1]

for power in range(0, 1000):
    index = len(digits) - 1
    while index >= 0:
        if 2 * digits[index] < 10:
            digits[index] = digits[index] * 2
        else:
            temp = 2 * digits[index]
            digits[index] = temp % 10
            if index == len(digits) - 1:
                digits.append(1)
            else:
                digits[index + 1] = digits[index + 1] + 1
        index = index - 1


sum = 0
for number in digits:
    sum = sum + number

print sum

end = time.clock()
print end - start
