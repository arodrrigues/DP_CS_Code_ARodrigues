import math 

def isSemiPrime(num): 
    a = 0
  
    for i in range(2, int(math.sqrt(num)) + 1): 
        while num % i == 0: 
            num /= i 
            a += 1 
  
       
        if a >= 2:  
            break
    
    if(num > 1): 
        a += 1
  
    
    return a == 2
  

def semiprime(n): 
    if isSemiPrime(n) == True: 
        print("True") 
    else: 
        print("False") 
  

n = 6
semiprime(n) 
  
n = 8
semiprime(n)