import time

start = time.clock()

amicables = set()
amicableFirst = 1
while amicableFirst < 10000:
    if amicableFirst not in amicables:
        amicableHalf = amicableFirst / 2
        divisor = 1
        properDivisors = []
        while divisor <= amicableHalf:
            if amicableFirst % divisor == 0:
                properDivisors.append(divisor)
            divisor = divisor + 1
        amicableSecond = 0
        index = 0
        while index < len(properDivisors):
            amicableSecond = amicableSecond + properDivisors[index]
            index = index + 1
        if amicableFirst != amicableSecond:
            amicableHalf = amicableSecond / 2
            divisor = 1
            properDivisors = []
            while divisor <= amicableHalf:
                if amicableSecond % divisor == 0:
                    properDivisors.append(divisor)
                divisor = divisor + 1
            amicableSum = 0
            index = 0
            while index < len(properDivisors):
                amicableSum = amicableSum + properDivisors[index]
                index = index + 1
            if amicableSum == amicableFirst:
                amicables.add(amicableFirst)
                amicables.add(amicableSecond)
    amicableFirst = amicableFirst + 1


amicableSum = 0
for number in amicables:
    amicableSum = amicableSum + number

print amicableSum

end = time.clock()
print end - start
