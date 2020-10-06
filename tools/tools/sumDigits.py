'''
This function takes a single positive integer parameter and returns
the sum of the digits
Parameters: i >= 0
return: returns sum of the digits
preondition: i is a valid integer greater than 0
'''
def sumDigits(a):

	total = 0
	#Casting is the process of changing type. 
	a = str(a)  

	#Fundamental skill: Looping through string

	#Count, check, change
	for i in range(0, len(a),1):
		total = total + int(a[i])

	return total

#TESTING
print(sumDigits(57))
print(sumDigits(0))
print(sumDigits(227))