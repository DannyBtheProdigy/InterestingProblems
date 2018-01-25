number : Int
number = 1
sum : Int
sum = 0

test : (mod3 : Int) -> (mod5 : Int) -> Bool
test mod3 mod5 = ((mod3 == 0) || (mod5 == 0))

loop : (number : Int) -> (sum : Int) -> Int
loop mod3 = modInt number 3
loop mod5 = modInt number 5
loop result with (test mod3 mod5)
	loop sum = (sum + number) | result = True
loop number with (number + 1)
	loop number sum = loop number sum	| number < 1000
	loop number sum = sum	 		| number >= 1000

main : IO()
main result = loop 1 0
main = print result

