'''
This functions takes values in base 10 and converts it to base 2
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



'''
This function takes a value in base 2 and converts it to base 10
Parameters: n
return: int
'''
def base2To10(str):

	n = 0
	total = 0

	for i in range(len(str -1, -1, -1)):  #loops through length of the string backwards
		total = total + int(str[i]) * 2**n 
		n = n + 1  

	return total

#TESTING
print(base2To10("101"))




'''
Desctription: This fucntion takes a string, representing a binary 
value and converts it to hexadecimal.
Parameter: string s
Return: string

'''
def base2ToHex(s):

	#declaring a list of strings called HEX and initializing
	#all elements to HEX characters
	HEX = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

	#Declares and initializes result to "", stores hex value
	result = ""

	#adds appropriate amount of zeros to make length of s / by 4
	s =  len(s)%4 * "0" + s

	#counted loop , looping through s by 4
	for i in range(0, len(s),4):

		#substring acceses 4 characters and stores result in v
		v = s[i: i + 4]

		#casting strings to integer values
		index = int(v[0])*8 + int(v[1])*4 + int(v[2])*2 + int(v[3])*1
		
		#convert base 2 number to base 10 to use the index as HEX value
		result = result + HEX[index]

	
	return result

#TESTING

BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]


for i in range (0, len(BIN),1):
	print(base2ToHex(BIN[i]))

print(base2ToHex("1011110101"))


'''
Description: this function takes a single hexadecimal 
character and returns the 4 digit binary representation
Parameteres: string s
return: string


'''
def hexToBase2_B(s):   #defines hexToBase_2 at string s
	result = ""

	DIC = { "0":"0000",     #dictionary stores HEX and BIN
			"1":"0001",
			"2":"0010",
			"3":"0011",
			"4":"0100",
			"5":"0101",
			"6":"0110",
			"7":"0111",
			"8":"1000",
			"9":"1001",
			"A":"1010",
			"B":"1011",
			"C":"1100",
			"D":"1101",
			"E":"1110",
			"F":"1111"}

	
	for i in range(0, len(s), 1):  # loops through the length of s 
                                    # and adds result from dictionary at i
		result = result + DIC[s[i]]

	return result


print(hexToBase2_B("0"))       #tests
print(hexToBase2_B("A6"))
print(hexToBase2_B("C"))



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


'''
Description: 
Write a method called findModSum1.  The method takes a list of integers.  
The method returns the sum of all the elements that are multiples of 3.
Name: findModSum1
Parameters: int[] data
Returns: int
Preconditions: data is a list of integers. 
findModSum1({21,4,6,9,10,12}) → 21 + 6 + 9 + 12 = 48
'''

def findModSum1(data):

	sum = 0

	#loop through each element
	for i in range(0, len(data), 1):

		#check if element is a multiple of 3
		if (data[i] % 3 == 0):
			sum = sum + data[i] #add element if multiple of three


	return sum

a = [41,4,8,12,2,10]
b = []
c = [7]
d = [3,3,3,3,3]

print(findModSum1(a))



'''
Description: 
Write a method called findModSum2.  The method takes a list of integers and 
two integer values.  The method returns the sum of all the elements that 
are between a (exclusive) and b (exclusive). 
Name: findModSum2
Parameters: int[] data, int a, int b
Returns: int
Preconditions: data is a list of integers a and b are both integers. 
'''

def findModSum2 (lst,a,b):
    sums = 0  #set sums to 0

    for i in range (len(lst)):  #loop through all elements
        if lst[i] > a and lst[i] < b:  #finds if values are in between a nd b
            sums = sums + lst[i]   #adds the correct values to sums

    return sums

#TESTING 
   
samplelist = []
samplelist = [3,4,9]
samplelist = [1,2,3,4,5,6,7,8,9,10]
print(findModSum2(samplelist,3,9))


''' 
This function takes a list of integers and two integer values. The function 
returns the sum of all values taht are divisble by a and b.
Parameters int[] lst, int a, int b
return int

precondition: a and b not equal to zero
post conditions: the list remains unchanged 
'''

def findModSum3(lst,a,b):
    
    sums = 0    #assignment statement 

    for i in range (0, len(lst), 1):  #loops through the length of lst
                                      #by increments of 1
        if lst[i] % a ==0 and lst[i] % b ==0:  #uses mod to discovers values 
                #in lst that are divisble by a then b by finding 0 remainder
            sums = sums + lst[i]  #adds the correct values to sums

    return sums

#TESTING

samplelist = []
samplelist = [2,3,10,9,14,25,3,100]

print(findModSum3(samplelist,2,5))
print(findModSum3(samplelist,6,27))



'''
Description: Takes a list of doubles and returns the sum 
of the digits
Parameters: double[] data
Returns: int
findModSum4({1.2,3.14,7.89}) → 1 + 2 + 3 + 1 + 4 + 7 + 8 + 9 = 35 
'''

def findModSum4(data):

	sum = 0
	#First loop will loop through the elements of data
	for i in range(0, len(data),1):

		a = data[i]
		a = str(a) #casts a to string 
		a = a.replace(".","")

		for j in range(0, len(a),1):

			v = a[j]
			v = int(v) #casts v to an integer
			sum = sum + v

	return sum

a = [1.2,3.14,7.89]
a = [4.234,3.00,7,2.53]

print(findModSum4(a))


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

    a = "" #sets a to an empty string

    for i in range (0, len(s), 1):  #loops through elements in s

        word = s[i]  #sets word to the elements in strings

       #loops backwards through word
        for j in range (len(word) - 1, -1, -1): 

            a = a + word[j]   #presenest elements in word in reveres to a

    return a

#TESTING

a = ["cat","dog"]
a = ["god","tac"]

print(reverseWordB(a))





