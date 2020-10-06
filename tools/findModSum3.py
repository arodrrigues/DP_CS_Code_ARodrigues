

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

