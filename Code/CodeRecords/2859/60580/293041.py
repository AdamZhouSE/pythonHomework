size = int(input())
i = 0
myList = []
while i < size:
    l = list(input())
    myList.append(l)
    i += 1
str = myList[0][0]
i = 0
while i < size:
    if myList[i][i] != str:
        print("NO")
        break
    i += 1
if i == size:
    j = 0
    while j < size:
        if myList[j][size - 1 - j] != str:
            print("NO")
            break
        j += 1
    if j == size:
        newList = []
        a = 0
        while a < size:
            b = 0
            while b < size:
                if myList[a][b] not in newList:
                    newList.append(myList[a][b])
                b += 1
            a += 1
        if len(newList) != 2:
            print("NO")
        else:
            print("YES")