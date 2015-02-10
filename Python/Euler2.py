import time

start = time.clock()

fibonacci1 = 1
fibonacci2 = 2
nextFibonacci = fibonacci1 + fibonacci2
sum = 2
while nextFibonacci < 4000000:
    if nextFibonacci % 2 == 0:
        sum = sum + nextFibonacci
    fibonacci1 = fibonacci2
    fibonacci2 = nextFibonacci
    nextFibonacci = fibonacci1 + fibonacci2

print sum

end = time.clock()
print end - start
