
import math

def findArea():

#input
#casting to float - changes type
'''
x1 = input()
x1 = float(x1)

y1 = input()
y1 = float(y1)

x2 = input()
x2 = float(x2)

y2 = input()
y2 = float(y2)

'''

#Contest Strategy - just ste variable values and take inputs after
x1 = 2
y1 = 4
x2 = 4
y2 = 8

#process
# r = ((y2 - y1)**(2) + (x2 - x1)**(2))**(1/2)
'''
sqrt is a static function contained in the math module.
static function does not require an implied object.

word = "Emanuel"
word.upper() #word is the implied object
math.sqrt(7) # math is a module containing a bunch of cuntion - no implied object 
is needed for sqrt to run. Therefor we incoke the method with the name of the module (or nothing)
#method runs purly on the parameters that are passes

'''
r = math.sqrt((y2 - y1)**(2) + (x2 - x1)**(2))
a = 3.14159*r*r
a = round(a,3)

print(a)

#Contest Strtegy - write the problem as a function
findArea()