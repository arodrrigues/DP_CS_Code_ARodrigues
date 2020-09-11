'''
This function takes a single positive integer parameter and 
returns the sum of the digits
Parameters: i >=0
return: sum of the digits

precondition i is a valid integer greater than 0
'''

def sumDigits(a):

    total = 0
    # Casting is the process of changing type (in this case an int to a str)
    a = str(a) # casting

    # Fundamental skill: Looping through string

    #Count, check, change
    for i in range(0, len(a),1):
        total = total + int(a[i])

    #Trace Table

    return(total)

'''
This function takes a single positive integer parameter and 
returns the sum of the digits
Parameters: i >=0
return: sum of the digits

precondition i is a valid integer greater than 0
'''

def sumDigitsA(a):

    while (a > 0):
        total = total + a % 10 #access the ones digit
        a = a // 10

        #Trace
    
    return total


print(sumDigitsA(57))




