import time
import math

start = time.clock()

potentialPrime = 2
primes = []
flag = False

while potentialPrime < 1000000:
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

prime_set = set()

for p in primes:
    prime_set.add(p)

count = 0

for prime in prime_set:
    prime_string = repr(prime)
    length = len(prime_string)
    index = 0
    all_good = True
    while((index < length) and (all_good == True)):
        if((int(prime_string[index:length] + prime_string[0:index])) not in prime_set):
           all_good = False
           
        index = index + 1

    if(all_good == True):
        count = count + 1

print(count)

end = time.clock()
print end - start
