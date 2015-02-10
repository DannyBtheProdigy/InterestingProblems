import time

start = time.clock()

number = 600851475143
half = number / 2
test = 2
while test < half:
    if number % test == 0:
        number = number / test
        half = number / 2
        test = 2
    else:
        test = test + 1

print number

end = time.clock()
print end - start
