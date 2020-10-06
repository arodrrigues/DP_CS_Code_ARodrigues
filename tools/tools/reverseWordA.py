'''
Description: Write a method called reverseWordA. The method takes 
a Strings and returns the string in reverse 
Parameters: String s
Returns: String
Precondition: s is a valid string of any length.
reverseWordA(“cat”) → “tac”
'''

def reverseWordA(s):

	a = "" #sets a to an empty string

	#loop through the stirng in reverse, by increments of -1
	for i in range(len(s) - 1, -1, -1):

		a = a + s[i] #adds the values of the string in reverse

	return a

#TESTING
print(reverseWordA("zebra"))
print(reverseWordA("d o g"))
print(reverseWordA(""))
