
def readFileToList(name):

    # Open is a function that takes two string parameters and returns
    # a reference to the file. Open is in Phyhons standard library
    file = open(name,"r")

    #create a new list called result which is empty
    result = []

    for line in file:
    result = readFileToList("sample.txt")