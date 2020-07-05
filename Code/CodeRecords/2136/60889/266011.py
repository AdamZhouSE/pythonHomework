numA = int(input())
system = 1
while True:
    system = system + 1
    judge = True
    numN = 1
    numL = system
    while judge:
        if numN < numA:
            numN = numN + numL
            numL = numL * system
        elif numN == numA:
            judge = False
            break
        else:
            break
    if judge==False:
        break
print(system)