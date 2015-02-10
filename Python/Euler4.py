import time

start = time.clock()

palindrome = [9, 9, 9, 9, 9, 9]
number1 = 999
while True:
    numericPalindrome = palindrome[0]*100000 + palindrome[1]*10000 + palindrome[2]*1000 + palindrome[3]*100 + palindrome[4]*10 + palindrome[5]
    if (numericPalindrome / number1) > 1000:
        number1 = 999
        if palindrome[2] > 0:
            palindrome[2] = palindrome[3] = palindrome[2] - 1
        else:
            palindrome[2] = palindrome[3] = 9
            if palindrome[1] > 0:
                palindrome[1] = palindrome[4] = palindrome[1] - 1
            else:
                palindrome[1] = palindrome[4] = 9
                palindrome[0] = palindrome[5] = palindrome[0] - 1
    else:
        if numericPalindrome % number1 == 0:
            break
        else:
            number1 = number1 - 1

print palindrome

end = time.clock()
print end - start
