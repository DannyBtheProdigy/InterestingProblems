import time

start = time.clock()

nameFile = open('p022_names.txt')
nameString = nameFile.readline()
nameList = nameString.split('","')
nameList[0] = nameList[0].split('"')[1]
nameList[len(nameList) - 1] = nameList[len(nameList) -1].split('"')[0]
nameList.sort()

index = 0
score = 0
while index < len(nameList):
    name = nameList[index]
    nameSum = 0
    for character in name:
        nameSum = nameSum + (ord(character) - 64)
    score = score + nameSum * (index + 1)
    index = index + 1

print score

end = time.clock()
print end - start
