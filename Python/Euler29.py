import time
import math

start = time.clock()

a = 2
b = 2
group = set()

while a <= 100:
    while b <= 100:
        group.add(math.pow(a, b))
        b = b + 1
    b = 2
    a = a + 1

print len(group)

end = time.clock()
print end - start
