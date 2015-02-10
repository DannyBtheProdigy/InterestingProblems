numbers = []
luckyNumbers = [1]

numToAdd = 1
while numToAdd < 500:
    if numToAdd % 2 == 0:
        numbers.append(False)
    else:
        numbers.append(True)
    numToAdd = numToAdd + 1


while len(luckyNumbers) < 50:
    count = 0
    start = 0
    index = 0
  
    while count <= len(luckyNumbers) and index < 499:
        if numbers[index] == True:
            count = count + 1
        index = index + 1
    
    start = index
    
    luckyNumbers.append(start)
    index = 0
    count = 0
    while index < 499:
        if numbers[index] == True:
            count = count + 1
        if count == start:
            numbers[index] = False
            count = 0
        index = index + 1


print luckyNumbers
    
