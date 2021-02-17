
def convertTime(time):


    h = time[0:2]
    h = int(h)
    m = time[3:5]
    m = int(m)
    print(h)
    x = "AM"  #assume AM

    if (12 <= h <= 23):
        x = "PM"
        h = h - 12

#is there a process we can apply to convert either case
    print(str(h)+":"+str(m)+" PM")


convertTime("09:30")