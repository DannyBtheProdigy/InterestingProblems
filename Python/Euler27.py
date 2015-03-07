import time
import math

start = time.clock()

a = -999
b = -999
maxA = 0
maxB = 0
maxPrimes = 0
primes = set()

while a < 1000:
    while b < 1000:
        n = 0
        flag = 0
        numPrimes = 0
        while flag == 0:
            result = n * n + a * n + b
            if result in primes:
                numPrimes = numPrimes + 1
                n = n + 1
                continue
            root = math.sqrt(abs(result))
            divisor = 2
            isPrime = 1
            while divisor <= root:
                if result % divisor == 0:
                    isPrime = 0
                    flag = 1
                divisor = divisor + 1
            if isPrime == 1:
                primes.add(result)
                numPrimes = numPrimes + 1
            n = n + 1
        if numPrimes > maxPrimes:
            maxPrimes = numPrimes
            maxA = a
            maxB = b
        b = b + 1
    a = a + 1
    b = -999

print maxA * maxB
            

end = time.clock()
print end - start
