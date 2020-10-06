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



