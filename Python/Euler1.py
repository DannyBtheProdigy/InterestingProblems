import time

start = time.clock()

number = 1
sum = 0
while number < 1000:
	if (number % 3 == 0) or (number % 5 == 0):
		sum = sum + number
	number = number + 1

print sum
end = time.clock()
print end - start
