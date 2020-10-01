def reverseWordB(s):

    a = ""

    for i in range (0, len(s), 1):

        word = s[i]

        for j in range (len(word) - 1, -1, -1):
            a = a + word[j]

    return a

a = ["cat","dog"]
print(reverseWordB(a))

