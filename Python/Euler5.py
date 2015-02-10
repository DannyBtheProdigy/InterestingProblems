import time

start = time.clock()

number = 2
divisor = 2
adder = 2

while divisor < 21:
    if number % divisor == 0:
        divisor = divisor + 1
        adder = number
    else:
        number = number + adder

print number

end = time.clock()
print end - start
