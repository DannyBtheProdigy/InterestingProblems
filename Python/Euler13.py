import time

start = time.clock()

inputSet = []

with open('Euler13Input.txt') as inputs:
    for line in inputs:
        newNumber = []
        for digit in line:
            if digit != '\n':
                newNumber.append((int)(digit))
        newNumber.reverse()
        inputSet.append(newNumber)

sum = inputSet[0]

row = 1
while row < len(inputSet):
    line = inputSet[row]
    column = 0
    while column < len(line):
        sum[column] = sum[column] + line[column]
        column = column + 1
    digit = 0
    while digit < len(sum):
        if sum[digit] >= 10:
            if digit == len(sum) - 1:
                sum.append(sum[digit] / 10)
            else:
                sum[digit + 1] = sum[digit + 1] + sum[digit] / 10
            sum[digit] = sum[digit] % 10
        digit = digit + 1

    row = row + 1

sum.reverse()

print sum[0:10]

end = time.clock()
print end - start
