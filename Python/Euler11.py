import time

start = time.clock()

matrix = []

with open('Euler11Input.txt') as matrixDoc:
    for line in matrixDoc:
        elements = line.split()
        row = []
        for item in elements:
            row.append(int(item))
        matrix.append(row)

row = 0
column = 0
greatestProduct = 0
while row < 20:
    while column < 20:
        product = 0
        if row + 3 < 20:
            product = matrix[row][column] * matrix[row + 1][column] * matrix[row + 2][column] * matrix[row + 3][column]
            if product > greatestProduct:
                greatestProduct = product
        if column + 3 < 20:
            product = matrix[row][column] * matrix[row][column + 1] * matrix[row][column + 2] * matrix[row][column + 3]
            if product > greatestProduct:
                greatestProduct = product
        if (row + 3) < 20 and (column + 3) < 20:
            product = matrix[row][column] * matrix[row + 1][column + 1] * matrix[row + 2][column + 2] * matrix[row + 3][column + 3]
            if product > greatestProduct:
                greatestProduct = product
        if (row + 3) < 20 and (column - 3) >= 0:
            product = matrix[row][column] * matrix[row + 1][column - 1] * matrix[row + 2][column - 2] * matrix[row + 3][column - 3]
            if product > greatestProduct:
                greatestProduct = product
        column = column + 1
    row = row + 1
    column = 0

print greatestProduct

end = time.clock()
print end - start
