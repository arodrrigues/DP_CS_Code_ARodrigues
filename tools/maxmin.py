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