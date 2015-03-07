import time

start = time.clock()

starter = 1
count = 0
while starter < 10000:
    iteration = 1
    flag = False
    number = starter
    while iteration < 50:
        numString = str(number)
        index = len(numString) - 1
        reversed = ''
        while index >= 0:
            reversed = reversed + numString[index]
            index = index - 1
        if reversed == numString and iteration != 1:
            flag = True
            break
        else:
            number = int(reversed) + number
        iteration = iteration + 1
    if flag == False:
        count = count + 1
    starter = starter + 1

print count

end = time.clock()
print end - start
