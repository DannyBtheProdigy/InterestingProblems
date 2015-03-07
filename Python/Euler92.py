import time

start = time.clock()

startingNumber = 2
chainValues = set()
while startingNumber < 10000000:
    currentChain = set()
    number = startingNumber
    while number != 89 or number != 1:
        

end = time.clock()
print end - start
