num = int(input())


def printnum(x):
    if x == 1:
        print(str(x), end=" ")
    else:
        printnum(x - 1)
        if x == n:
            print(str(x), end=" \n")
        else:
            print(str(x), end=" ")


for i in range(num):
    n = int(input())
    printnum(n)