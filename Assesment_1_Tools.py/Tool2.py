'''
This program uses a linear search to search through an array and discover animals
parameters: arr, n, x
return: str
Preconditions: arr contains length
'''

def search(arr, n, x): 
  
    for i in range (0, n, 1): 
        if (arr[i] == x): 
            return i 
    return -1

arr = [ 'dog','cat','hamster','gorilla','mouse','lizard','parrot','moose', 'bear'] 
x = 'moose' 
a = 'bear'
n = len(arr) 
result = search(arr, n, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("I once saw a" , str(x), "in Algonquin Park")
    print("I have also seen a" , str(a), "in Banff National Park")
    print(len(arr))