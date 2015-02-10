import time

start = time.clock()

matrix = []

with open('p081_matrix.txt') as matrixDoc:
    for line in matrixDoc:
        elements = line.split(',')
        row = []
        for item in elements:
            row.append(int(item))
        matrix.append(row)

#matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]

elementsToExplore = []
explored = set()

row = 0
while row < 79:
    startingTuple = matrix[row][0], row, 0
    elementsToExplore.append(startingTuple)
    row = row + 1

while True:
    elementsToExplore.sort()
    if elementsToExplore[0][2] == 79:
        break
    row = elementsToExplore[0][1]
    column = elementsToExplore[0][2]
    coordinate = row, column
    explored.add(coordinate)
    if row < 79:
        newElement = elementsToExplore[0][0] + matrix[row + 1][column], row + 1, column
        coordinate = newElement[1], newElement[2]
        if coordinate not in explored:
            elementsToExplore.append(newElement)
    if column < 79:
        newElement = elementsToExplore[0][0] + matrix[row][column + 1], row, column + 1
        coordinate = newElement[1], newElement[2]
        if coordinate not in explored:
            elementsToExplore.append(newElement)
    if row > 0:
        newElement = elementsToExplore[0][0] + matrix[row - 1][column], row - 1, column
        coordinate = newElement[1], newElement[2]
        if coordinate not in explored:
            elementsToExplore.append(newElement)
    
    elementsToExplore.pop(0)
    

print elementsToExplore[0][0]

end = time.clock()
print end - start
