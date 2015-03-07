import time

start = time.clock()

matrix = []

row = 0
column = 0
while row < 100:
    newRow = []
    while column < 200:
        newRow.append(0)
        column = column + 1
    matrix.append(newRow)
    column = 0
    row = row + 1

left = (200 / 2) - 1
row = 0

with open('p067_triangle.txt') as matrixDoc:
    for line in matrixDoc:
        elements = line.split()
        if row == 0:
            matrix[row][left] = (int)(elements[0])
            left = left - 1
            row = row + 1
            continue
        index = 0
        while index < len(elements):
            leftPath = (int)(elements[index]) + matrix[row - 1][left + (2 * index) - 1]
            rightPath = (int)(elements[index]) + matrix[row - 1][left + (2 * index) + 1]
            matrix[row][left + 2 * index] = max(leftPath, rightPath)
            index = index + 1
        row = row + 1
        left = left - 1

print max(matrix[len(matrix) - 1])

end = time.clock()
print end - start
