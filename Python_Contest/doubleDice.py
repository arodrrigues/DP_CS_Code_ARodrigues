

def double_dice():

    #creates an input for number or rounds and list of dice rolls
    rounds = input()
    count_list = []
    
    #sets David and Antonia's starting scores at 100
    antonia = 100
    david = 100

    #uses a for loop to run through inputed list and split lines at return 
    # as well as append the lst to count_list
    for i in range(int(rounds)):
        line = input()
        lst = line.split()
        count_list.append(lst)

    #uses a for loop to run through inputed # of rounds andcompare greater or less than scores
    #subtracts the greater score from player with the lesser score
    #j[0] being the first inputed dice role representing Antonia
    #j[1] being the second inputed dice role representing David
    for j in range(int(rounds)):
        if count_list[j][0] > count_list[j][1]:
            david -= int(count_list[j][0])
        elif count_list[j][0] == count_list[j][1]:
            pass
        else:
            antonia -= int(count_list[j][1])

    #prints final values for David and Antonia
    print(antonia)
    print(david)


double_dice()

