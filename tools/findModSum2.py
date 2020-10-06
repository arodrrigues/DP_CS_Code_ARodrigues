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