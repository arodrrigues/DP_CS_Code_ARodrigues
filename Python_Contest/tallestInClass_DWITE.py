'''
    val = data[i]
    while True:



        try:
            loc = val.index(" ")
            data1.append(val[0:loc])
            val = val[loc+1:]
        except:
            data1.appen(val)

    print(data1)


        data = ["Jim 1.45 m",
        ]
    '''
'''
def convertToMeters (units, height, names):
    allInMeters = []
    for k in range(0, len(units), 1):
        if inits[k] == "m":
            allInMeters.append(float(height[k]))
        elif units[k] == "dm":
            newhheight = float(height[k]) / 10
            allInMeters.append(newheight)
        elif units[k] == "cm":
            newheight = float(height[k]) / 100
            allInMeters.append(newheight)
        else:
            newheight = float(height[k]) / 1000
            allInMeters.append(newheight)
        return allInMeters

def tallestProblem ():
    text = "12 Jim 1.45 m Sally 187 cm Joey 1064 mm Roel 15.23 dm Karl 13 cm Melanie 18.9 dm Jill 1.54 m Sam 133 cm"
    sublist = text.split()
    names = []
    height = []
    units = []
    for i in range(1, len(sublist), 3):
        names.append(sublist[i])
    for l in range(2, len(sublist), 3):
        height.append(sublist[l])
    for n in range(3, len(sublist), 3):
        units.append(sublist[n])
    names2 = []
    allInMeters = convertToMeters(units, height, names, names2)
    namesFinal = []
    values = []

    for i in range(0, 5):
        max1 = max(allInMeters)
        indexof = allInMeters.index(max1)
        values.append(allInMetes[indexof])
        namesFinal.append(names2[indexof])
        allInMeters.remove(allInMeters[indexof])
        names2.remove(names2[indexof])
    for i in range(len(namesFinak)):
        print(namesFinal[i])

    '''

#this finction takes a float value representing a meausurement value and a string representing the units.
#the function returns -1 if the unit is not recognized

'''
def findMeters(val, unit):

    if val < 0:
        return -1
    if unit == "mm":
        return val/1000
    elif unit == "cm":
        return val/100
    elif unit == "dm":
        return val/10
    elif unit == "m":
        return val/1

    return -1

print(findMeters(99,"nm"))

'''

'''
This method converts the passed value from u1 to u2 where
val is a float, u1 and u2 are string values.
'''

def convertUnits(val,u1,u2):

    factor = ["mm","cm","dm","m"]

    v1 = factor.index(u1)
    v2 = factor.index(u2)

    print(v1)
    print(v2)

    conv = v2 - v1

    return val/(10**conv)

print(convertUnits(100,"mm","cm"))