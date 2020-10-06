'''
fins the maximum and minimum values in a list
paramenters: lst
return: 

'''
l = [100,2,3]
#abstraction: this is the process of hiding how something is done. 
print(max(l))

'''
WATCH: 
'''
def findMaxConcern(a):

    
    a.sort() #If I sort the list from lowest to highest
    return a[len(a) - 1]

l = [100,2,3]
w = l #give w and l the same refernce. 
z = l.copy()

print("L = ",l)

m = findMaxConcern(l)
print(m)
print(l)
print("W =",w)

'''
findMax takes list of integers and returns max value.
The list a must contain at least 1 element and a must
remain unchanged when the function is done. 
'''
def findMax(a):

    #Big Idea: Set the correct value to an element in the list
    m = a[0]
    for i in range(0,len(a),1):
        m = max(m,a[i]) #max is OVERLOADED method

    return m

l = [100,2,3]
m = findMax(l)
print(m)
print(l) #l not changed


'''
isEven takes a single integer parameter a >= 0 returning true
if a is even and false if a is odd
'''
def isEven(a):

	if a % 2 == 0:
		return True

	return False

print(isEven(0))
print(isEven(10))
print(isEven(9))

'''
Codingbat Problem
'''
def missing_char(str, n):
	
	return str[0:n] + str[n + 1:len(str)]
 

def first_last6(nums):
  
  
  if (nums[0] == 6 or nums[len(nums) - 1] == 6):
    return True
  
  return False

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))

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

print(sumDigits(123))
print(sumDigits(0))
print(sumDigits(4))

'''
Definition: takes two integers a and b and returns the sum
parameters int a, int b
preconditions: 
'''
def addNum(a,b):
	return a + b


print(countDigits2(1234))
print("TEST")


'''
This method takes two lists and returns a new list containing
the common elements from both lists.
parameters: l1, l2
returns: lst
'''
def commonElements(l1,l2):

	l3 = []

	for i in range(0, len(l1),1):

		for j in range(0, len(l2),1):

			if l1[i] == l2[j]:
				l3.append(l1[i])

	return l3

l1 = ["cat","dog","fish","monkey","cat"]
l2 = ["monkey","cat","moose"]