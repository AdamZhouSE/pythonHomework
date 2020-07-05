def printLine(x):
    for j in range(0, int((n - x) / 2)):
        print("*",end="")
    for j in range(0, x):
        print("D",end="")
    for j in range(0, int((n - x) / 2)):
        print("*",end="")
    print()


n = int(input())
for i in range(1, n + 1, 2):
    printLine(i)
for i in range(n-2, 0, -2):
    printLine(i)