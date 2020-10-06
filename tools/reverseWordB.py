'''
Description: The method takes a list of Strings and returns a 
new string of each word constructed in reverse.  
Parameters: String[] s
Returns: String
Precondition: s is a list of any length and it contains strings 
of any length
reverseWordB({“cat”,”dog”}) → “tacgod”
'''
def reverseWordB(s):

    a = "" #sets a to an empty string

    for i in range (0, len(s), 1):  #loops through elements in s

        word = s[i]  #sets word to the elements in strings

       #loops backwards through word
        for j in range (len(word) - 1, -1, -1): 

            a = a + word[j]   #presenest elements in word in reveres to a

    return a

#TESTING

a = ["cat","dog"]
a = ["god","tac"]

print(reverseWordB(a))

