'''
This functions takes values in base 10 and converts them to base 2
Parameters: n
return: int
'''
def base10ToBase2(n):

	result = ""  # declares and initializes resilt to ""

	while n > 0:  #loops through n if n is greater than zero

		result = str(n % 2) + result #result equals resukt str at n mod 2
		n = n//2  #integer divide n by 2

	return result

#TESTING
print(base10ToBase2(53))
print(base10ToBase2(4))
print(base10ToBase2(113))

