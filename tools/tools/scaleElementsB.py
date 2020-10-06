'''
Write a function called scaleElementsB that takes an integer value 
a and a list/array reference b.  The function should create a new 
list/array with an equal length of b with each element scaled by a.
 The parameter b should not be changed. For example if the list is 
 [1,2,3,4] and the scale factor a = 2. This means that the returned 
 array should be [2,4,6,8]. The postcondition of a should be that 
 the array is not changed. 

Name: scaleElementsB

Parameters: int, int[]

Return: int[]

'''

def scaleElementsB(a,b):
	print("Scale Elements B")
	c = [] #creates an empty list

	for i in range(0, len(b),1):
		c.append(b[i]*a) #append adds a new element to the list

	return c

print("START TEST CODE SCALE ELEMENTS A")
l = [1,2,3,4]
print(l)
scaleElementsB(2,l)
print(l)


print("**********")