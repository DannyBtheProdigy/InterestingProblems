import time
import math

start = time.clock()

potentialPrime = 2
primes = []
flag = False

while potentialPrime < 2000000:
    if potentialPrime / 2 == 1:
        primes.append(potentialPrime)
    else:
        root = math.sqrt(potentialPrime)
        for p in primes:
            if p > root:
                break;
            if potentialPrime % p == 0:
                flag = True
                break;
        if not flag:
            primes.append(potentialPrime)
        flag = False

    potentialPrime = potentialPrime + 1

sum = 0
for p in primes:
    sum = sum + p

print sum

end = time.clock()
print end - start
