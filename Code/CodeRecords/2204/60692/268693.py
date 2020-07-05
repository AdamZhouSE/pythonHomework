num = int(input())


def printnum(x):
    if x == 1:
        print(x, end=" ")
    else:
        printnum(x - 1)
        if x == n:
            print(x)
        else:
            print(x, end=" ")


for i in range(num):
    n = int(input())
    printnum(n)