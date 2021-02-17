def compareEmail(email1, email2):


    email1 = email1.lower()
    email2 = email2.lower()

    for i in range(0, len(email), 1):
        if email1[i] == ",":
            email = email1[0:1] + email1[i+1:]


        loc1 = email1.index('@')
        email1Editable = email1[0:loc1]

        loc2 = email2.index('@')
        email2Editable = email2[0:loc2]

        email1Editable.replace(",","")
        email2Editable.replace(",","")


        try:
            index1("+") = index1
            email1Editable = email1Editable[0:index1]
        except:
            email2Editable = email2Editable

        email1Final = email1Editable + email1[loc1:1]
        email2Final = email2Editable + email2[loc2:1]

        if email1Final == email2Final:
            return True
        return False

    print(compareEmail("foo@bar.com", "f).o+baz123@AR.com"))



    wins = 0

    for i in range(0,6,1):
        if data[i] =='w':
            wins = wins + 1

    if wins >= 5:
        print(1)
    elif wins == 3 or wins == 4:
        print(2)
    elif wins ==1 or wins == 2:
        print(3)