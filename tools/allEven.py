
def isEven(n):

    even = True

    while (n > 0) and (even == True):
        if (n % 10) % 2 == 1:
            even = False
        n = n // 10
        print(n)
    return even

print(isEven(345))
print(isEven(246))


