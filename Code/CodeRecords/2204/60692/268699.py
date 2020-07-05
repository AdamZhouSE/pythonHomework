num = int(input())


def printnum(x):
    if x == 1:
        print(x, end=" ")
    else:
        printnum(x - 1)
        print(x, end=" ")
        if x == n:
            print("\n")


for i in range(num):
    n = int(input())
    printnum(n)