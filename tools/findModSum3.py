def findModSum3(lst,a,b):
    sums = 0

    for i in range (len(lst)):
        if lst[i] % a ==0 and lst[i] % b ==0:
            sums = sums + lst[i]

    return sums
samplelist = [2,3,10,9,14,25,3,100]
print(findModSum3(samplelist,2,5))
