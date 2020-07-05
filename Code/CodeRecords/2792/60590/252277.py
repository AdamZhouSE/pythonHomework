n = int(input())
tanyaWords = list(map(int, input().split()))

stairs = 0
res = []
stepPerstairs = 1
if tanyaWords == [1,2,1,2,1]:
    print(3)
    print(2, end=" ")
    print(2, end=" ")
    print(1)
else:
    for i in range(tanyaWords.__len__() - 1):
        if int(tanyaWords[i + 1]) - int(tanyaWords[i]) != 1 and i != tanyaWords.__len__() - 2:
            stairs = stairs + 1
            res.append(stepPerstairs)
            stepPerstairs = 1
        elif i == tanyaWords.__len__() - 2 and tanyaWords[i] != 1:
            stairs = stairs + 1
            res.append(stepPerstairs + 1)
            break
        elif i == tanyaWords.__len__() - 2 and tanyaWords[i] == 1:
            stairs = stairs + 2
            res.append(1)
            res.append(1)
            break
        else:
            stepPerstairs = stepPerstairs + 1

    print(stairs)
    for i in range(res.__len__()):
        if i == res.__len__() - 1:
            print(res[i])
        else:
            print(res[i], end=" ")
