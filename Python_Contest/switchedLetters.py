def switchedLetters():

    word = input()

    for i in range(0,len(word),1):
        if word[i] != 'I' and word[i] != 'O' and word[i] != 'S' and word[i] != 'H' and word[i] != 'Z' and word[i] != 'X' and word[i] != 'N':
            print("NO")
            return

    print("YES")

print(switchedLetters())

