'''
This conditions merges two strings]
parameters: String [] a, String[] b
return: String[]
'''

def mergeStrings(a,b):
    c=[]  #creating empty list
    if (len(a)>=len(b)):  #comparing sizes of list a and b and storing n value
        n=len(b)  #store n value
        l=len(a)  #store l value
        y=0
    else:
        n=len(a)
        l=len(b)
        y=1
    for i in range(0,n):  #looping from 0 to n
        x=a[i]+b[i]    #merging elements a and b
        c.append(x)    #appending element to the list
    if(y==0):

        for j in range(i+1,n):  #appending remaining elements in list a
            c.append(a[j])  
    else:
        for j in range(i+1,l):  #appending remaining elements in list b
            c.append(b[j])
    return c  #returning list c

a= []
#creating 2 empty lists at a and b
b= []

#collecting number of elements as input
n= int(input("Enter number of elements in list 1: "))
print("Enter elements of list 1:")

#looping through range of n
for i in range(0, n):
    e = input()  #collecting input as elements in string a
    a.append(e)  #appending element
l= int(input("Enter number of elements in list 2: "))
print("Enter elements of list 2:")

#looping through range of l
for i in range(0, l):
    e = input()    #collecting input as elements in string b
    b.append(e) #appending element

c = mergeStrings(a,b)  #calling mergeString function
print(c) 
 
