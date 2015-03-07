import time

start = time.clock()

row = 0
column = 0
matrix = []
while row < 21:
    newRow = []
    while column < 21:
        newRow.append(1)
        column = column + 1
    matrix.append(newRow)
    row = row + 1
    column = 0

row = 19
column = 19
while row >= 0:
    while column >= 0:
        matrix[row][column] = matrix[row + 1][column] + matrix[row][column + 1]
        column = column - 1
    row = row - 1
    column = 19

print matrix[0][0]

end = time.clock()
print end - start
