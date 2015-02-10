import time

start = time.clock()

startingNumber = number = 1
longestChain = currentChain = 0
bestStart = 0
chainList = set()
flag = True

while startingNumber < 1000000:
    if startingNumber not in chainList:
        while number > 1:
            currentChain = currentChain + 1
            chainList.add(number)
            if number % 2 == 0:
                number = number /2
            else:
                number = 3 * number + 1
    if currentChain > longestChain:
        longestChain = currentChain
        bestStart = startingNumber
    currentChain = 0
    number = startingNumber = startingNumber + 1
    flag = True

print bestStart

end = time.clock()
print end - start
