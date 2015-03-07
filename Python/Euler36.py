import time

start = time.clock()

n = 1
sum = 0
while n < 1000000:
    decimal = str(n)
    length = len(decimal)
    index = length - 1
    reversed = ''
    flag = False

    while index >= 0:
        reversed = reversed + decimal[index]
        index = index - 1
    if reversed == decimal:
        binary = bin(n).split('b')[1]
        length = len(binary)
        index = length - 1
        reversed = ''
        while index >= 0:
            reversed = reversed + binary[index]
            index = index - 1
        if reversed == binary:
            flag = True
    if flag == True:
        sum = sum + n
    n = n + 1

print sum

end = time.clock()
print end - start
