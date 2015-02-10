import time

start = time.clock()

potentialPrime = 2
primes = []
flag = False

while len(primes) < 10001:
    if potentialPrime / 2 == 1:
        primes.append(potentialPrime)
    else:
        half = potentialPrime / 2
        for p in primes:
            if p > half:
                break;
            if potentialPrime % p == 0:
                flag = True
                break;
        if not flag:
            primes.append(potentialPrime)
        flag = False

    potentialPrime = potentialPrime + 1

print potentialPrime - 1

end = time.clock()
print end - start
