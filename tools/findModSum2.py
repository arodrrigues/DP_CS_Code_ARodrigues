def findModSum2 (lst,a,b):
    sums = 0

    for i in range (len(lst)):
        if lst[i] > a and lst[i] < b:
            sums = sums + lst[i]

    return sums
samplelist = [1,2,3,4,5,6,7,8,9,10]
print(findModSum2(samplelist,3,9))