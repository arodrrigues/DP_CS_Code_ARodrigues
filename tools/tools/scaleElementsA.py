
'''
Write a function called scaleElementsA that takes an integer value
 a and a list/array reference b.  The function should scale each 
 element of b. For example if the list is [1,2,3,4] and the scale 
 factor a = 2. This means that the postcondition of the function 
 is that the list/array is set to [2,4,6,8].

Name: scaleElementsA

Parameters: int, int[]

Return: none
'''


def scaleElementsA(a, b):
	print("Scale Elements A")

	#I need to loop through every element and multiply it by a
	for i in range(0,len(b),1):
		# if b = [1,2,3,4], i will be 0,1,2,3
		b[i]= a * b[i] #b[i] is sai "b at i"

	
print("START TEST CODE SCALE ELEMENTS A")
l = [1,2,3,4]
print(l)
scaleElementsA(2,l)
print(l)


print("**********")

