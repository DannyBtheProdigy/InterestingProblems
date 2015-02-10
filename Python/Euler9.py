import time

start = time.clock()

number = 1000
a = 0
b = 0
c = 0
flag = True
while flag:
    a = a + 1
    b = a + 1
    half = number / 2
    while a + b < number:
        c = number - a - b
        cSquared = c * c
        sum = (a * a) + (b * b)
        if sum == cSquared:
            flag = False
            break;
        b = b + 1

product = a * b * c
print product

end = time.clock()
print end - start
