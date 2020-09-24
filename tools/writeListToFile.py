def writeListToFile(name,a):

    file = open(name,"a")

    for i in range(len(a)):
        file.write(a[i]+"\n")

    file.close()


strings = ["dad " ,"mom " ,"cat " ,"dog " ]

writeListToFile("test.txt",strings)