'''
Description: The method takes a list of Strings and returns a 
new string of each word constructed in reverse.  
Parameters: String[] s
Returns: String
Precondition: s is a list of any length and it contains strings 
of any length
reverseWordB({“cat”,”dog”}) → “tacgod”
'''
def reverseWordB(s):

    a = "" #sets a to an empty string, a string is a dynamic data structure
			# a string is a reference data type as it stores locations for where the data is stored

    for i in range (0, len(s), 1):  #loops through elements in s starting from 0 by increments of 1

        word = s[i]  #sets variable word to the elements in strings

       #loops backwards through word 
	   #starts at -1 (last element) and loops by increments of -1 (backwards)
        for j in range (len(word) - 1, -1, -1): 

            a = a + word[j]   #Self referencing statement presents a as reverse

    return a  #returns a as string

#TESTING

a = ["cat","dog "]
#output "tac god"
s = ["tac","god "]
#output "cat dog"
b = [""]
#output nothing


print(reverseWordB(a))
print(reverseWordB(s))
print(reverseWordB(b))

