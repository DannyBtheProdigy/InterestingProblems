import time
import math

start = time.clock()

fibonacci1 = 1
fibonacci2 = 1
nextFibonacci = fibonacci1 + fibonacci2
term = 3

while math.log10(nextFibonacci) < 999:
    fibonacci1 = fibonacci2
    fibonacci2 = nextFibonacci
    nextFibonacci = fibonacci1 + fibonacci2
    term = term + 1

print term

end = time.clock()
print end - start
