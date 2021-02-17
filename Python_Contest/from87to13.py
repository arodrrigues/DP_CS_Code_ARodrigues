

def double_dice():
    rounds = input()
    count_list = []
    antonia = 100
    david = 100

    for i in range(int(rounds)):
        line = input()
        lst = line.split()
        count_list.append(lst)

    for j in range(int(rounds)):
        if count_list[j][0] > count_list[j][1]:
            david -= int(count_list[j][0])
        elif count_list[j][0] == count_list[j][1]:
            pass
        else:
            antonia -= int(count_list[j][1])
    print("Antonia's final score " + str(antonia))
    print("Davids final score " + str(david))


double_dice()