import time
import math
from decimal import *

start = time.clock()

getcontext().prec = 10000

max_cycle = 1
max_denom = 2

denominator = 2
while denominator < 1000:
    decimal = Decimal(1) / Decimal(denominator)
    decimal_string = repr(decimal)[11:]
    decimal_string_length = len(decimal_string) - 3
    decimal_string = decimal_string[:decimal_string_length]

    index = 0
    length = 1
    cycle_found = False
    while((cycle_found == False) and (length < (decimal_string_length / 2))):
        sub_string = decimal_string[(decimal_string_length - length):decimal_string_length]
        if(sub_string == decimal_string[(decimal_string_length - (2 * length)):(decimal_string_length - length)]):
            cycle_found = True
        else:
            length = length + 1

    if(cycle_found == True):
        if(length > max_cycle):
            max_cycle = length
            max_denom = denominator

              
    denominator = denominator + 1

print(max_denom)

end = time.clock()
print end - start
