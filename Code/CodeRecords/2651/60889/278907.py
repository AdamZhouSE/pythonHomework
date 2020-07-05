numOfInput = int(input())
for i in range(numOfInput):
    numI = int(input())
    numO = 0
    judge = True
    j = 1
    while numI != 0:
        if numI % 2 == 1:
            if judge:
                numO = numO + j * 2
            else:
                numO = numO + int(j / 2)
        j = j * 2
        numI = int(numI/2)
        judge = not(judge)
    print(numO)