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