import time

start = time.clock()

digits = []
integer = 1

while(len(digits) < 1000000):
    integer_string = repr(integer)
    for digit in integer_string:
        digits.append(int(digit))
    
    integer = integer + 1


product = digits[0] * digits[9] * digits[99] * digits[999] * digits[9999] * digits[99999] * digits[999999]

print(product)
    
end = time.clock()
print end - start
