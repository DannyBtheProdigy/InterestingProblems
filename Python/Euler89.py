import time

start = time.clock()

savedDigits = 0
with open('p089_roman.txt') as numeralText:
    for line in numeralText:
        startLength = len(line)
        line = line.replace('VIIII', 'IX')
        line = line.replace('IIII', 'IV')
        line = line.replace('LXXXX', 'XC')
        line = line.replace('XXXX', 'XL')
        line = line.replace('DCCCC', 'CM')
        line = line.replace('CCCC', 'CD')
        endLength = len(line)
        savedDigits = savedDigits + (startLength - endLength)
            
print savedDigits

end = time.clock()
print end - start
