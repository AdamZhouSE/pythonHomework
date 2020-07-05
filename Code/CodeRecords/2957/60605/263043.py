s = input().strip()

liOfDuplicatedStrings = []
cnt = 0
current = None
for i in list(s):
    if i != current:
        if current != None:
            liOfDuplicatedStrings.append(current*cnt)
        current = i
        cnt = 1
    else:
        cnt += 1
if cnt > 0:
    liOfDuplicatedStrings.append(current*cnt)

if len(liOfDuplicatedStrings) == 1:
    print(len(liOfDuplicatedStrings[0]))
else:
    setOfTars = set([])
    for i in range(0, len(liOfDuplicatedStrings)-1):
        for j in range(len(liOfDuplicatedStrings[i])+1):
            for k in range(len(liOfDuplicatedStrings[i+1])+1):
                setOfTars.add(liOfDuplicatedStrings[i][0]*j+liOfDuplicatedStrings[i+1][0]*k)

    # for i in liOfDuplicatedStrings:
    #     nn = len(i)
    #     dup = i[0]
    #     for i in range(nn, 0, -1):
    #         if dup*i not in setOfTars:
    #             setOfTars.add(dup*i)
    #         else:
    #             break

    print(len(setOfTars)-1)