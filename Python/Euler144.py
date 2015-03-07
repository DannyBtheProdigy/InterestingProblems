import time
import math

start = time.clock()

origin = (0.0, 10.1)
destination = (1.4, -9.6)
slope = (destination[1] - origin[1]) / (destination[0] - origin[0])
reflections = 1


while True:
    tangentSlope = -4 * destination[0] / destination[1]
    normalSlope = -1 / tangentSlope
    normalSquared = normalSlope * normalSlope
    reflectionSlope = (2 * normalSlope - slope + normalSquared * slope) / (1 + 2 * normalSlope * slope - normalSquared)
    slope = reflectionSlope
    offset = destination[1] - slope * destination[0]
    origin = destination
    a = slope * slope + 4
    b = 2 * slope * offset
    c = offset * offset - 100
    insideRoot = b * b - 4 * a * c
    denominator = 2 * a
    negNumerator = -b - math.sqrt(insideRoot)
    posNumerator = -b + math.sqrt(insideRoot)
    negx = negNumerator / denominator
    posx = posNumerator / denominator
    if abs(negx - origin[0]) > abs(posx - origin[0]):
        destination = (negx, slope * negx + offset)
    else:
        destination = (posx, slope * posx + offset)
    if destination[0] > -0.01 and destination[0] < 0.01 and destination[1] > 9.0:
        break
    reflections = reflections + 1

print reflections
          

end = time.clock()
print end - start
