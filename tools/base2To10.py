def base2To10(str):

	n = 0
	total = 0

	for i in range(len(str -1, -1, -1)):  #loops through length of the string backwards
		total = total + int(str[i]) * 2**n 
		n = n + 1  

	return total

#TESTING
print(base2To10("101"))